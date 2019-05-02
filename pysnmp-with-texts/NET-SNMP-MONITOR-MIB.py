#
# PySNMP MIB module NET-SNMP-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-MONITOR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:18:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
netSnmpObjects, netSnmpModuleIDs = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpObjects", "netSnmpModuleIDs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, MibIdentifier, ObjectIdentity, ModuleIdentity, TimeTicks, Counter32, Bits, IpAddress, Gauge32, NotificationType, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Counter32", "Bits", "IpAddress", "Gauge32", "NotificationType", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netSnmpMonitorMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 3))
netSnmpMonitorMIB.setRevisions(('2002-02-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmpMonitorMIB.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: netSnmpMonitorMIB.setLastUpdated('200202090000Z')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setContactInfo('postal: Wes Hardaker P.O. Box 382 Davis CA 95617 email: net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmpMonitorMIB.setDescription('Configured elements of the system to monitor (XXX - ugh! - need a better description!)')
nsProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 21))
nsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 22))
nsFile = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 23))
nsLog = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 24))
mibBuilder.exportSymbols("NET-SNMP-MONITOR-MIB", nsFile=nsFile, nsProcess=nsProcess, PYSNMP_MODULE_ID=netSnmpMonitorMIB, netSnmpMonitorMIB=netSnmpMonitorMIB, nsLog=nsLog, nsDisk=nsDisk)
