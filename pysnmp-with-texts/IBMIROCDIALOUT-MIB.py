#
# PySNMP MIB module IBMIROCDIALOUT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMIROCDIALOUT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ObjectIdentity, IpAddress, Counter64, MibIdentifier, Integer32, Unsigned32, Bits, TimeTicks, ModuleIdentity, iso, Gauge32, NotificationType, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ObjectIdentity", "IpAddress", "Counter64", "MibIdentifier", "Integer32", "Unsigned32", "Bits", "TimeTicks", "ModuleIdentity", "iso", "Gauge32", "NotificationType", "NotificationType", "Counter32")
RowStatus, DisplayString, TruthValue, TextualConvention, PhysAddress, AutonomousType, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention", "PhysAddress", "AutonomousType", "TestAndIncr")
ibmIROCroutingDialOut = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6))
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm2210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 72))
ibmIROC = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119))
ibmIROCrouting = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4))
ibmDialOutTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 0))
ibmDialOutMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1))
ibmDialOutDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 2))
ibmDialOutConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3))
ibmDialOutGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 1))
dialOutCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 1))
dialOutGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 2))
dialOutIfTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2), )
if mibBuilder.loadTexts: dialOutIfTable.setStatus('mandatory')
dialOutIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dialOutIfEntry.setStatus('mandatory')
dialOutIfUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutIfUserName.setStatus('mandatory')
if mibBuilder.loadTexts: dialOutIfUserName.setDescription('could be null.')
dialOutIfTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutIfTimeRemaining.setStatus('mandatory')
if mibBuilder.loadTexts: dialOutIfTimeRemaining.setDescription('The amount of time the connection allowed. Zero means no limits.')
dialOutIfInactivityTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutIfInactivityTimer.setStatus('mandatory')
if mibBuilder.loadTexts: dialOutIfInactivityTimer.setDescription('The amount of time the connection is in inactivity state.')
dialOutIfDTRState = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("noChange", 0), ("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutIfDTRState.setStatus('mandatory')
dialOutIfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("undefined", 1), ("hose", 2), ("telnet", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutIfProtocol.setStatus('mandatory')
dialOutEnableComport = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutEnableComport.setStatus('mandatory')
dialOutSendBinary = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutSendBinary.setStatus('mandatory')
dialOutSupressGoAhead = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutSupressGoAhead.setStatus('mandatory')
dialOutDisableEcho = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialOutDisableEcho.setStatus('mandatory')
dialOutPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialOutPortName.setStatus('mandatory')
if mibBuilder.loadTexts: dialOutPortName.setDescription("By setting the value to a string of zero length will reset the value of this obejct to the node default value, usuallly is 'ALL_PORTS'.")
dialOutIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 2, 1))
dialOutCoreCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 6, 3, 1, 1))
mibBuilder.exportSymbols("IBMIROCDIALOUT-MIB", dialOutCoreCompliance=dialOutCoreCompliance, dialOutIfTimeRemaining=dialOutIfTimeRemaining, dialOutCompliances=dialOutCompliances, ibmDialOutTraps=ibmDialOutTraps, dialOutIfProtocol=dialOutIfProtocol, dialOutIfUserName=dialOutIfUserName, dialOutIfInactivityTimer=dialOutIfInactivityTimer, dialOutIfDTRState=dialOutIfDTRState, ibmDialOutConformance=ibmDialOutConformance, ibmProd=ibmProd, ibmDialOutGeneral=ibmDialOutGeneral, ibm=ibm, dialOutSupressGoAhead=dialOutSupressGoAhead, dialOutDisableEcho=dialOutDisableEcho, ibmIROCrouting=ibmIROCrouting, ibmDialOutDomains=ibmDialOutDomains, dialOutIfGroup=dialOutIfGroup, dialOutPortName=dialOutPortName, ibmIROC=ibmIROC, dialOutEnableComport=dialOutEnableComport, dialOutGroups=dialOutGroups, ibmIROCroutingDialOut=ibmIROCroutingDialOut, dialOutSendBinary=dialOutSendBinary, dialOutIfEntry=dialOutIfEntry, ibm2210=ibm2210, ibmDialOutMIB=ibmDialOutMIB, dialOutIfTable=dialOutIfTable)
