//
//  Helper.swift
//  2023-01-AOC
//
//  Created by John Peden on 12/1/23.
//

import Foundation

struct Helper {
    static func read(filename: String) -> String {
        if let directory = FileManager.default.urls(
            for: .desktopDirectory,
            in: .userDomainMask
        ).first {
            
            let filePath = directory.appending(component: "aoc/\(filename)")
            
            do {
                return try String(contentsOf: filePath)
            } catch (let err) {
                print(err)
            }
        }
        
        return ""
    }
}
