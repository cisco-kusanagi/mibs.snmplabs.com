#
# PySNMP MIB module RBTWS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:45:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Counter64, ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, Unsigned32, NotificationType, Gauge32, iso, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter64", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "iso", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbtwsExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7))
rbtwsExternalServerMib.setRevisions(('2006-07-31 00:04',))
if mibBuilder.loadTexts: rbtwsExternalServerMib.setLastUpdated('200609271237Z')
if mibBuilder.loadTexts: rbtwsExternalServerMib.setOrganization('Enterasys Networks')
class RbtwsIpPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class RbtwsSyslogServerEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

rbtwsExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1))
rbtwsExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1))
rbtwsExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: rbtwsExtServerSyslogTable.setStatus('current')
rbtwsExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogIndex"))
if mibBuilder.loadTexts: rbtwsExtServerSyslogEntry.setStatus('current')
rbtwsExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rbtwsExtServerSyslogIndex.setStatus('current')
rbtwsExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogAddress.setStatus('current')
rbtwsExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 3), RbtwsIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogPort.setStatus('current')
rbtwsExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 4), RbtwsSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogEnable.setStatus('current')
rbtwsExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2))
rbtwsExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1))
rbtwsExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2))
rbtwsExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1, 1)).setObjects(("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsExternalServerCompliance = rbtwsExternalServerCompliance.setStatus('current')
rbtwsExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2, 1)).setObjects(("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogAddress"), ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogPort"), ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsExternalServerConfigGroup = rbtwsExternalServerConfigGroup.setStatus('current')
mibBuilder.exportSymbols("RBTWS-EXTERNAL-SERVER-MIB", rbtwsExternalServerCompliances=rbtwsExternalServerCompliances, rbtwsExtServerSyslogPort=rbtwsExtServerSyslogPort, RbtwsSyslogServerEnable=RbtwsSyslogServerEnable, rbtwsExtServerSyslogAddress=rbtwsExtServerSyslogAddress, RbtwsIpPort=RbtwsIpPort, rbtwsExternalServerGroups=rbtwsExternalServerGroups, rbtwsExternalServerMib=rbtwsExternalServerMib, rbtwsExtServerSyslogEnable=rbtwsExtServerSyslogEnable, rbtwsExternalServerCompliance=rbtwsExternalServerCompliance, rbtwsExtServerSyslogTable=rbtwsExtServerSyslogTable, rbtwsExternalServerConfigGroup=rbtwsExternalServerConfigGroup, rbtwsExtServerSyslogEntry=rbtwsExtServerSyslogEntry, rbtwsExtServerSyslogIndex=rbtwsExtServerSyslogIndex, rbtwsExternalServerDataObjects=rbtwsExternalServerDataObjects, rbtwsExternalServerObjects=rbtwsExternalServerObjects, rbtwsExternalServerConformance=rbtwsExternalServerConformance, PYSNMP_MODULE_ID=rbtwsExternalServerMib)
