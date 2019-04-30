#
# PySNMP MIB module WAN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WAN-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:28:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
extremenetworks, extremeAgent = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremenetworks", "extremeAgent")
dsx1LineStatus, dsx1IfIndex, dsx1LineIndex = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus", "dsx1IfIndex", "dsx1LineIndex")
dsx3IfIndex, dsx3LineIndex, dsx3LineStatus = mibBuilder.importSymbols("RFC1407-MIB", "dsx3IfIndex", "dsx3LineIndex", "dsx3LineStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysDescr, sysUpTime = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr", "sysUpTime")
NotificationType, iso, Gauge32, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, Counter64, Counter32, IpAddress, Bits, TimeTicks, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Gauge32", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "Counter32", "IpAddress", "Bits", "TimeTicks", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wanDsx1LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,100)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx1LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,101)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx1NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,102)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1406-MIB", "dsx1LineIndex"), ("RFC1406-MIB", "dsx1IfIndex"), ("RFC1406-MIB", "dsx1LineStatus"))
wanDsx3LineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,103)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
wanDsx3LossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,104)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
wanDsx3NoLossOfMasterClock = NotificationType((1, 3, 6, 1, 4, 1, 1916) + (0,105)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysDescr"), ("RFC1407-MIB", "dsx3LineIndex"), ("RFC1407-MIB", "dsx3IfIndex"), ("RFC1407-MIB", "dsx3LineStatus"))
mibBuilder.exportSymbols("WAN-TRAP-MIB", wanDsx1LossOfMasterClock=wanDsx1LossOfMasterClock, wanDsx3NoLossOfMasterClock=wanDsx3NoLossOfMasterClock, wanDsx1LineStatusChange=wanDsx1LineStatusChange, wanDsx3LossOfMasterClock=wanDsx3LossOfMasterClock, wanDsx3LineStatusChange=wanDsx3LineStatusChange, wanDsx1NoLossOfMasterClock=wanDsx1NoLossOfMasterClock)
