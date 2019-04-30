#
# PySNMP MIB module NET-SNMP-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
netSnmpModuleIDs, netSnmpObjects = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpModuleIDs", "netSnmpObjects")
Float, = mibBuilder.importSymbols("NET-SNMP-TC", "Float")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, IpAddress, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, Counter32, MibIdentifier, Integer32, ModuleIdentity, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "IpAddress", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "Counter32", "MibIdentifier", "Integer32", "ModuleIdentity", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 4))
netSnmpSystemMIB.setRevisions(('2002-02-09 00:00',))
if mibBuilder.loadTexts: netSnmpSystemMIB.setLastUpdated('200202090000Z')
if mibBuilder.loadTexts: netSnmpSystemMIB.setOrganization('www.net-snmp.org')
nsMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 31))
nsSwap = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 32))
nsCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 33))
nsLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 34))
nsDiskIO = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 35))
mibBuilder.exportSymbols("NET-SNMP-SYSTEM-MIB", netSnmpSystemMIB=netSnmpSystemMIB, nsLoad=nsLoad, nsDiskIO=nsDiskIO, nsCPU=nsCPU, nsMemory=nsMemory, nsSwap=nsSwap, PYSNMP_MODULE_ID=netSnmpSystemMIB)
