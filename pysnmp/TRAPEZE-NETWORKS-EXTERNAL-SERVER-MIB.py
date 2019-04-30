#
# PySNMP MIB module TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, iso, Integer32, Bits, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress, ObjectIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "iso", "Integer32", "Bits", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
TrpzIpPort, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzIpPort")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 7))
trpzExternalServerMib.setRevisions(('2011-06-22 00:40', '2009-10-02 00:21', '2008-10-24 00:10', '2006-07-31 00:04',))
if mibBuilder.loadTexts: trpzExternalServerMib.setLastUpdated('201106220040Z')
if mibBuilder.loadTexts: trpzExternalServerMib.setOrganization('Trapeze Networks')
class TrpzSyslogServerEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

trpzExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1))
trpzExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1))
trpzExternalServerGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2))
trpzExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: trpzExtServerSyslogTable.setStatus('current')
trpzExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogIndex"))
if mibBuilder.loadTexts: trpzExtServerSyslogEntry.setStatus('current')
trpzExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: trpzExtServerSyslogIndex.setStatus('current')
trpzExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSyslogAddress.setStatus('current')
trpzExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 3), TrpzIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSyslogPort.setStatus('current')
trpzExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 4), TrpzSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSyslogEnable.setStatus('current')
trpzExtServerPrimaryDnsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerPrimaryDnsIpAddress.setStatus('current')
trpzExtServerSecondaryDnsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSecondaryDnsIpAddress.setStatus('current')
trpzExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2))
trpzExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1))
trpzExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2))
trpzExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerCompliance = trpzExternalServerCompliance.setStatus('obsolete')
trpzExternalServerComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1, 2)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExternalServerConfigGroup"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExternalServerDnsServerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerComplianceRev2 = trpzExternalServerComplianceRev2.setStatus('current')
trpzExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogAddress"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogPort"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerConfigGroup = trpzExternalServerConfigGroup.setStatus('current')
trpzExternalServerDnsServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2, 2)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerPrimaryDnsIpAddress"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSecondaryDnsIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerDnsServerGroup = trpzExternalServerDnsServerGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", trpzExternalServerConformance=trpzExternalServerConformance, PYSNMP_MODULE_ID=trpzExternalServerMib, trpzExternalServerGlobalObjects=trpzExternalServerGlobalObjects, trpzExternalServerComplianceRev2=trpzExternalServerComplianceRev2, trpzExternalServerConfigGroup=trpzExternalServerConfigGroup, TrpzSyslogServerEnable=TrpzSyslogServerEnable, trpzExtServerSyslogEnable=trpzExtServerSyslogEnable, trpzExternalServerCompliances=trpzExternalServerCompliances, trpzExtServerSyslogAddress=trpzExtServerSyslogAddress, trpzExternalServerObjects=trpzExternalServerObjects, trpzExtServerSyslogPort=trpzExtServerSyslogPort, trpzExternalServerMib=trpzExternalServerMib, trpzExtServerSyslogIndex=trpzExtServerSyslogIndex, trpzExternalServerGroups=trpzExternalServerGroups, trpzExtServerPrimaryDnsIpAddress=trpzExtServerPrimaryDnsIpAddress, trpzExtServerSyslogEntry=trpzExtServerSyslogEntry, trpzExternalServerDnsServerGroup=trpzExternalServerDnsServerGroup, trpzExternalServerDataObjects=trpzExternalServerDataObjects, trpzExternalServerCompliance=trpzExternalServerCompliance, trpzExtServerSyslogTable=trpzExtServerSyslogTable, trpzExtServerSecondaryDnsIpAddress=trpzExtServerSecondaryDnsIpAddress)
