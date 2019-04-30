#
# PySNMP MIB module NET-SNMP-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-MONITOR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
netSnmpModuleIDs, netSnmpObjects = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpModuleIDs", "netSnmpObjects")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Gauge32, Unsigned32, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, ModuleIdentity, Counter32, Counter64, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Gauge32", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "ModuleIdentity", "Counter32", "Counter64", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netSnmpMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 3))
netSnmpMonitorMIB.setRevisions(('2002-02-09 00:00',))
if mibBuilder.loadTexts: netSnmpMonitorMIB.setLastUpdated('200202090000Z')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setOrganization('www.net-snmp.org')
nsProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 21))
nsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 22))
nsFile = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 23))
nsLog = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 24))
mibBuilder.exportSymbols("NET-SNMP-MONITOR-MIB", netSnmpMonitorMIB=netSnmpMonitorMIB, PYSNMP_MODULE_ID=netSnmpMonitorMIB, nsProcess=nsProcess, nsDisk=nsDisk, nsLog=nsLog, nsFile=nsFile)
