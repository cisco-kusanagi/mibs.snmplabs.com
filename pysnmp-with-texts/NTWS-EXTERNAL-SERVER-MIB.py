#
# PySNMP MIB module NTWS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NtwsIpPort, = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsIpPort")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, Integer32, NotificationType, TimeTicks, ObjectIdentity, IpAddress, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "Integer32", "NotificationType", "TimeTicks", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7))
ntwsExternalServerMib.setRevisions(('2008-10-24 00:10', '2007-08-16 00:05', '2006-07-31 00:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsExternalServerMib.setRevisionsDescriptions(("v1.1.0: Factored out 'NtwsIpPort' textual convention (was moved to the new module Basic TC).", 'v1.0.5, MRT v1: Made changes in order to make MIB compile cleanly and comply with corporate MIB conventions.', 'v1.0.4: Initial version',))
if mibBuilder.loadTexts: ntwsExternalServerMib.setLastUpdated('200810240010Z')
if mibBuilder.loadTexts: ntwsExternalServerMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsExternalServerMib.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsExternalServerMib.setDescription("External Server configuration MIB. Copyright 2008 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsSyslogServerEnable(TextualConvention, Integer32):
    description = 'Syslog Server mode (administratively enabled or disabled).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

ntwsExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1))
ntwsExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1))
ntwsExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: ntwsExtServerSyslogTable.setStatus('current')
if mibBuilder.loadTexts: ntwsExtServerSyslogTable.setDescription('Configured Syslog server table.')
ntwsExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogIndex"))
if mibBuilder.loadTexts: ntwsExtServerSyslogEntry.setStatus('current')
if mibBuilder.loadTexts: ntwsExtServerSyslogEntry.setDescription('Entry for Syslog server table.')
ntwsExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: ntwsExtServerSyslogIndex.setStatus('current')
if mibBuilder.loadTexts: ntwsExtServerSyslogIndex.setDescription('Index of the Syslog sever')
ntwsExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogAddress.setStatus('current')
if mibBuilder.loadTexts: ntwsExtServerSyslogAddress.setDescription('IP Address of the Syslog server.')
ntwsExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 3), NtwsIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogPort.setStatus('current')
if mibBuilder.loadTexts: ntwsExtServerSyslogPort.setDescription('The Syslog server Port number.')
ntwsExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 1, 1, 1, 4), NtwsSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsExtServerSyslogEnable.setStatus('current')
if mibBuilder.loadTexts: ntwsExtServerSyslogEnable.setDescription('The administrative status of the Syslog server (enabled/disabled)')
ntwsExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2))
ntwsExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1))
ntwsExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2))
ntwsExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 1, 1)).setObjects(("NTWS-EXTERNAL-SERVER-MIB", "ntwsExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsExternalServerCompliance = ntwsExternalServerCompliance.setStatus('current')
if mibBuilder.loadTexts: ntwsExternalServerCompliance.setDescription('The compliance statement for devices that implement the External Server MIB.')
ntwsExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 7, 1, 2, 2, 1)).setObjects(("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogAddress"), ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogPort"), ("NTWS-EXTERNAL-SERVER-MIB", "ntwsExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsExternalServerConfigGroup = ntwsExternalServerConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ntwsExternalServerConfigGroup.setDescription('Mandatory group of objects implemented to provide External Server configuration info.')
mibBuilder.exportSymbols("NTWS-EXTERNAL-SERVER-MIB", PYSNMP_MODULE_ID=ntwsExternalServerMib, ntwsExternalServerCompliance=ntwsExternalServerCompliance, ntwsExtServerSyslogAddress=ntwsExtServerSyslogAddress, ntwsExtServerSyslogIndex=ntwsExtServerSyslogIndex, ntwsExternalServerMib=ntwsExternalServerMib, NtwsSyslogServerEnable=NtwsSyslogServerEnable, ntwsExtServerSyslogPort=ntwsExtServerSyslogPort, ntwsExternalServerConfigGroup=ntwsExternalServerConfigGroup, ntwsExternalServerCompliances=ntwsExternalServerCompliances, ntwsExtServerSyslogEntry=ntwsExtServerSyslogEntry, ntwsExtServerSyslogTable=ntwsExtServerSyslogTable, ntwsExtServerSyslogEnable=ntwsExtServerSyslogEnable, ntwsExternalServerDataObjects=ntwsExternalServerDataObjects, ntwsExternalServerConformance=ntwsExternalServerConformance, ntwsExternalServerGroups=ntwsExternalServerGroups, ntwsExternalServerObjects=ntwsExternalServerObjects)
