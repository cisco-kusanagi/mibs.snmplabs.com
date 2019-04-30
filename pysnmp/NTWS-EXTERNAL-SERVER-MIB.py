#
# PySNMP MIB module NTWS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NtwsIpPort, = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsIpPort")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Bits, IpAddress, Counter32, ObjectIdentity, iso, Counter64, ModuleIdentity, NotificationType, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "IpAddress", "Counter32", "ObjectIdentity", "iso", "Counter64", "ModuleIdentity", "NotificationType", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7))
ntwsExternalServerMib.setRevisions(('2008-10-24 00:10', '2007-08-16 00:05', '2006-07-31 00:04',))
if mibBuilder.loadTexts: ntwsExternalServerMib.setLastUpdated('200810240010Z')
if mibBuilder.loadTexts: ntwsExternalServerMib.setOrganization('Nortel Networks')
class NtwsSyslogServerEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

ntwsExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1))
ntwsExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1))
ntwsExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: ntwsExtServerSyslogTable.setStatus('current')
ntwsExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogIndex"))
if mibBuilder.loadTexts: ntwsExtServerSyslogEntry.setStatus('current')
ntwsExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ntwsExtServerSyslogIndex.setStatus('current')
ntwsExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogAddress.setStatus('current')
ntwsExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 3), NtwsIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogPort.setStatus('current')
ntwsExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 4), NtwsSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogEnable.setStatus('current')
ntwsExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2))
ntwsExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1))
ntwsExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2))
ntwsExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1, 1)).setObjects(("NTWS-EXTERNAL-SERVER-MIB", "ntwsExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsExternalServerCompliance = ntwsExternalServerCompliance.setStatus('current')
ntwsExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2, 1)).setObjects(("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogAddress"), ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogPort"), ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsExternalServerConfigGroup = ntwsExternalServerConfigGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-EXTERNAL-SERVER-MIB", ntwsExternalServerGroups=ntwsExternalServerGroups, ntwsExtServerSyslogEntry=ntwsExtServerSyslogEntry, ntwsExternalServerCompliance=ntwsExternalServerCompliance, ntwsExternalServerConformance=ntwsExternalServerConformance, ntwsExternalServerConfigGroup=ntwsExternalServerConfigGroup, ntwsExtServerSyslogTable=ntwsExtServerSyslogTable, ntwsExternalServerMib=ntwsExternalServerMib, ntwsExtServerSyslogAddress=ntwsExtServerSyslogAddress, ntwsExtServerSyslogEnable=ntwsExtServerSyslogEnable, ntwsExternalServerObjects=ntwsExternalServerObjects, PYSNMP_MODULE_ID=ntwsExternalServerMib, NtwsSyslogServerEnable=NtwsSyslogServerEnable, ntwsExtServerSyslogPort=ntwsExtServerSyslogPort, ntwsExternalServerDataObjects=ntwsExternalServerDataObjects, ntwsExtServerSyslogIndex=ntwsExtServerSyslogIndex, ntwsExternalServerCompliances=ntwsExternalServerCompliances)
