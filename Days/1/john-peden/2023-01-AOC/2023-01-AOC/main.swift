//
//  main.swift
//  2023-01-AOC
//
//  Created by John Peden on 12/1/23.
//

import Foundation

let result = Helper.read(filename: "day1/problem-1.txt")
    .components(separatedBy: .newlines)
    .map {
        $0.filter { $0.isNumber }
    }
    .compactMap {
        if !$0.isEmpty {
            let first: String = String($0.first!)
            let second: String = String($0.last!)
            
            return Int(first + second)
        }
        return nil
    }
    .reduce(0, +)

print(result)
    


    
