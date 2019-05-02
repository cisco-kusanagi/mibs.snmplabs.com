#
# PySNMP MIB module WAN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WAN-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
extremeAgent, extremenetworks = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent", "extremenetworks")
dsx1LineStatus, dsx1IfIndex, dsx1LineIndex = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus", "dsx1IfIndex", "dsx1LineIndex")
dsx3IfIndex, dsx3LineIndex, dsx3LineStatus = mibBuilder.importSymbols("RFC1407-MIB", "dsx3IfIndex", "dsx3LineIndex", "dsx3LineStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysDescr, sysUpTime = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr", "sysUpTime")
Counter64, Bits, NotificationType, Unsigned32, MibIdentifier, ObjectIdentity, NotificationType, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "NotificationType", "Unsigned32", "MibIdentifier", "ObjectIdentity", "NotificationType", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wanDsx1LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,100)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
if mibBuilder.loadTexts: wanDsx1LineStatusChange.setDescription('Signifies that the DS1 line status change for the specified interface has been detected.')
wanDsx1LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,101)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
if mibBuilder.loadTexts: wanDsx1LossOfMasterClock.setDescription('Signifies that the wanDsx1LossOfMasterClock event for the specified interface has been detected.')
wanDsx1NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,102)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
if mibBuilder.loadTexts: wanDsx1NoLossOfMasterClock.setDescription('Signifies that the wanDsx1NoLossOfMasterClock event for the specified interface has been detected.')
wanDsx3LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,103)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
if mibBuilder.loadTexts: wanDsx3LineStatusChange.setDescription('Signifies that the T3 line status change for the specified interface has been detected.')
wanDsx3LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,104)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
if mibBuilder.loadTexts: wanDsx3LossOfMasterClock.setDescription('Signifies that the wanDsx3LossOfMasterClock event for the specified interface has been detected.')
wanDsx3NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,105)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
if mibBuilder.loadTexts: wanDsx3NoLossOfMasterClock.setDescription('Signifies that the wanDsx3NoLossOfMasterClock event for the specified interface has been detected.')
mibBuilder.exportSymbols("WAN-TRAP-MIB", wanDsx1LineStatusChange=wanDsx1LineStatusChange, wanDsx1LossOfMasterClock=wanDsx1LossOfMasterClock, wanDsx3NoLossOfMasterClock=wanDsx3NoLossOfMasterClock, wanDsx3LossOfMasterClock=wanDsx3LossOfMasterClock, wanDsx3LineStatusChange=wanDsx3LineStatusChange, wanDsx1NoLossOfMasterClock=wanDsx1NoLossOfMasterClock)
