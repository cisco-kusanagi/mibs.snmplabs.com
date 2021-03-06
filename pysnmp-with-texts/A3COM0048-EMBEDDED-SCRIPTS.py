#
# PySNMP MIB module A3COM0048-EMBEDDED-SCRIPTS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0048-EMBEDDED-SCRIPTS
# Produced by pysmi-0.3.4 at Wed May  1 11:08:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
rmonExtensions, = mibBuilder.importSymbols("A3COM0004-GENERIC", "rmonExtensions")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
EntryStatus, OwnerString = mibBuilder.importSymbols("RMON-MIB", "EntryStatus", "OwnerString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, MibIdentifier, Counter64, IpAddress, ModuleIdentity, Integer32, NotificationType, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibIdentifier", "Counter64", "IpAddress", "ModuleIdentity", "Integer32", "NotificationType", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
command = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 10, 25, 5))
cmdMacroTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 1), )
if mibBuilder.loadTexts: cmdMacroTable.setStatus('mandatory')
if mibBuilder.loadTexts: cmdMacroTable.setDescription('Extended RMON table that provides a macro execution facility on the remote unit.')
cmdMacroEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 1, 1), ).setIndexNames((0, "A3COM0048-EMBEDDED-SCRIPTS", "cmdMacroIndex"))
if mibBuilder.loadTexts: cmdMacroEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cmdMacroEntry.setDescription('')
cmdMacroIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cmdMacroIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cmdMacroIndex.setDescription('Standard RMON index column.')
cmdMacroName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdMacroName.setStatus('mandatory')
if mibBuilder.loadTexts: cmdMacroName.setDescription('A short text name for this macro. This name can be referenced in the cmdTable to execute a script.')
cmdMacroString = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdMacroString.setStatus('mandatory')
if mibBuilder.loadTexts: cmdMacroString.setDescription('Text macro that is represented by this control entry.')
cmdMacroOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 1, 1, 4), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdMacroOwner.setStatus('mandatory')
if mibBuilder.loadTexts: cmdMacroOwner.setDescription('RMON Owner of this process.')
cmdMacroStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 1, 1, 5), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdMacroStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cmdMacroStatus.setDescription('Rmon RowStatus for this macro definition.')
cmdExecTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2), )
if mibBuilder.loadTexts: cmdExecTable.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecTable.setDescription("Extended RMON table that provides a script execution facility on the remote unit. Note that scripts executed by this table do not have to reside in the macro table. A script is identified by its 'cmdExecMacroName'. The agent will search all available script sources for that named script. The script _may_ be found in the macro table but this is not mandated.")
cmdExecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1), ).setIndexNames((0, "A3COM0048-EMBEDDED-SCRIPTS", "cmdExecUnit"), (0, "A3COM0048-EMBEDDED-SCRIPTS", "cmdExecIndex"))
if mibBuilder.loadTexts: cmdExecEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecEntry.setDescription('')
cmdExecUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cmdExecUnit.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecUnit.setDescription("Identifies one of a number of different 'execution units'. Genrally each of these is a separate processor in a distributed environment.")
cmdExecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: cmdExecIndex.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecIndex.setDescription('Standard RMON index column.')
cmdExecProcessStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inactive", 1), ("running", 2), ("suspended", 3), ("dying", 4), ("paused", 5), ("searching", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmdExecProcessStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecProcessStatus.setDescription("The current status of this process. The various possible values are described as follows: inactive : This process is not currently executing any script. This is the default state after creating a row in the table. running: The process is currently executing a script, and that script is not currently blocked by any internal asynchronous activity. 'running' actually means that this process is capable of being scheduled and is in a 'ready to run' scheduling queue. suspended: The script being executed by this process is currently blocked waiting for the completion of some asynchronous activity. dying: The script that was being executed by this process has completed and is waiting to be tidied up. When the tidyup has been completed this process will either automatically be destroyed or will enter the 'inactive' state. paused: The script being executed has been manually stopped, generally for debug purposes. A script can enter this state either voluntarily be requesting the system to stop it (ie similar to a breakpoint) or can be paused by writing to the cmdExecOperation variable. searching: When a process is given a script to execute the engine must first find that script. The script is identified by name (spe cified in cmdExecMacroName). The agent must search all possible sources for the script, which may take some time. The MIB allows the script to be specified by any name and so some implementations may allow the name to identify a file on some remote file system, for example by using a URL. While the agent searches for the script the process enters the 'searching' state. If the agent locates the script it will enter the 'running' state. If the script cannot be located then the process re-enters the 'inactive' state.")
cmdExecStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmdExecStartTime.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecStartTime.setDescription('sysUpTime when this process was started.')
cmdExecLastExecTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmdExecLastExecTime.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecLastExecTime.setDescription('sysUpTime when this process last used any processor time.')
cmdExecSystemTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmdExecSystemTime.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecSystemTime.setDescription('Number of time-ticks used by this process.')
cmdExecStatement = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmdExecStatement.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecStatement.setDescription('Generally scripts are broken into statements, this is just about true for any scripting mechanism. The statement number is generally useful for debugging. This object reports the current statement that will be executed _next_.')
cmdExecOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("execute", 2), ("suspend", 3), ("continue", 4), ("step", 5), ("kill", 6), ("Abort", 7), ("Next", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdExecOperation.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecOperation.setDescription("This object can be set to cause some action to be applied to a executing process. Note that this variable can only be set if the row- status is valid. Operations are: none - Value returned for _any_ read operation. execute - If the operational state of the macro is 'inactive' then this command will attempt to execute the script named in cmdMacroName. If the process is in any other state this command will be rejected. suspend - This command will suspend the process at the end of the current statement. Command is rejected if the macro is inactive. continue - If a macro is suspended due to a 'suspend' command this will cause it to continue execution from its current point. step - Execute the next statement and then stop. kill - Stop this process from running and put it in the inactive state. Note that this deletes all resource associated with the executing script, but not the process itself. abort - If the current macro status is 'suspended' Will cause it to terminate at its current point. next - Execute the next statement, stepping over child processes.")
cmdExecLastError = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36))).clone(namedValues=NamedValues(("none", 1), ("syntax", 2), ("noResource", 3), ("illegalAssignment", 4), ("blockMismatch", 5), ("badFnParams", 6), ("stackOverflow", 7), ("accessViolation", 8), ("typeMismatch", 9), ("nestTooDeep", 10), ("runTimeError", 11), ("noSuchVar", 12), ("outOfRange", 13), ("illegalLeftVal", 14), ("brokenRemoteProc", 15), ("sourceNotFound", 16), ("missingSemiColon", 17), ("missingEndList", 18), ("missingEndOid", 19), ("missingEndBracket", 20), ("missingEndSubscript", 21), ("missingEndParams", 22), ("invalidQuoteStr", 23), ("invalidGlobalName", 24), ("namedVarNotSupported", 25), ("processKilled", 26), ("childDiedBadly", 27), ("noTargetProcess", 28), ("invalidBinaryImage", 29), ("divideByZero", 30), ("parentDiedPadly", 31), ("nestedErrorHandler", 32), ("rpcTargetDoesnotExist", 33), ("rpcTargetNotSupported", 34), ("assertionFailed", 35), ("missingControlExpression", 36)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmdExecLastError.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecLastError.setDescription('Last error detected by this process or the script executing within the process.')
cmdExecOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 11), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdExecOwner.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecOwner.setDescription('RMON Owner of this process.')
cmdExecStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 12), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdExecStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecStatus.setDescription('Rmon RowStatus for this process.')
cmdExecMacroName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 25, 5, 2, 1, 13), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmdExecMacroName.setStatus('mandatory')
if mibBuilder.loadTexts: cmdExecMacroName.setDescription('Name of the script to execute in the process. The script can reside in either the macro table in this MIB module, or in some other internal script repository.')
mibBuilder.exportSymbols("A3COM0048-EMBEDDED-SCRIPTS", command=command, cmdExecProcessStatus=cmdExecProcessStatus, cmdExecStatus=cmdExecStatus, cmdMacroStatus=cmdMacroStatus, cmdExecOwner=cmdExecOwner, cmdExecOperation=cmdExecOperation, cmdExecLastExecTime=cmdExecLastExecTime, cmdExecTable=cmdExecTable, cmdExecStartTime=cmdExecStartTime, cmdExecStatement=cmdExecStatement, cmdMacroEntry=cmdMacroEntry, cmdMacroOwner=cmdMacroOwner, cmdMacroTable=cmdMacroTable, cmdMacroString=cmdMacroString, cmdExecLastError=cmdExecLastError, cmdExecMacroName=cmdExecMacroName, cmdExecUnit=cmdExecUnit, cmdExecIndex=cmdExecIndex, cmdExecSystemTime=cmdExecSystemTime, cmdMacroIndex=cmdMacroIndex, cmdExecEntry=cmdExecEntry, cmdMacroName=cmdMacroName)
