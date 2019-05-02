#
# PySNMP MIB module TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Unsigned32, Integer32, Counter32, Counter64, Bits, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Integer32", "Counter32", "Counter64", "Bits", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "NotificationType", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
TrpzIpPort, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzIpPort")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 7))
trpzExternalServerMib.setRevisions(('2011-06-22 00:40', '2009-10-02 00:21', '2008-10-24 00:10', '2006-07-31 00:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzExternalServerMib.setRevisionsDescriptions(('v1.4.0: Revised for 7.5 release.', 'v1.2.1: Added two scalars: trpzExtServerPrimaryDnsIpAddress, trpzExtServerSecondaryDnsIpAddress.', "v1.1.0: Factored out 'TrpzIpPort' textual convention (was moved to the new module Basic TC). This will be published in 7.1 release.", 'v1.0.4: Initial version, for 6.0 release',))
if mibBuilder.loadTexts: trpzExternalServerMib.setLastUpdated('201106220040Z')
if mibBuilder.loadTexts: trpzExternalServerMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzExternalServerMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzExternalServerMib.setDescription("External Server configuration MIB. Copyright 2006-2011 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzSyslogServerEnable(TextualConvention, Integer32):
    description = 'Syslog Server mode (administratively enabled or disabled).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

trpzExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1))
trpzExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1))
trpzExternalServerGlobalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2))
trpzExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: trpzExtServerSyslogTable.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerSyslogTable.setDescription('Configured Syslog server table.')
trpzExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogIndex"))
if mibBuilder.loadTexts: trpzExtServerSyslogEntry.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerSyslogEntry.setDescription('Entry for Syslog server table.')
trpzExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: trpzExtServerSyslogIndex.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerSyslogIndex.setDescription('Index of the Syslog sever')
trpzExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSyslogAddress.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerSyslogAddress.setDescription('IP Address of the Syslog server.')
trpzExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 3), TrpzIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSyslogPort.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerSyslogPort.setDescription('The Syslog server Port number.')
trpzExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 1, 1, 4), TrpzSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSyslogEnable.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerSyslogEnable.setDescription('The administrative status of the Syslog server (enabled/disabled)')
trpzExtServerPrimaryDnsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerPrimaryDnsIpAddress.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerPrimaryDnsIpAddress.setDescription('Configured IP address of the Primary DNS Server.')
trpzExtServerSecondaryDnsIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 1, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzExtServerSecondaryDnsIpAddress.setStatus('current')
if mibBuilder.loadTexts: trpzExtServerSecondaryDnsIpAddress.setDescription('Configured IP address of the Secondary DNS Server.')
trpzExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2))
trpzExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1))
trpzExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2))
trpzExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerCompliance = trpzExternalServerCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: trpzExternalServerCompliance.setDescription('The compliance statement for devices that implement the External Server MIB. This compliance statement was for releases 6.0 to 7.3 of AC (wireless switch) software. This compliance statement is replaced by trpzExternalServerComplianceRev2.')
trpzExternalServerComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 1, 2)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExternalServerConfigGroup"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExternalServerDnsServerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerComplianceRev2 = trpzExternalServerComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: trpzExternalServerComplianceRev2.setDescription('The compliance statement for devices that implement the External Server MIB. This compliance statement is for releases 7.5 and greater of AC (wireless switch) software.')
trpzExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogAddress"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogPort"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerConfigGroup = trpzExternalServerConfigGroup.setStatus('current')
if mibBuilder.loadTexts: trpzExternalServerConfigGroup.setDescription('Mandatory group of objects implemented to provide External Server configuration info.')
trpzExternalServerDnsServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 7, 1, 2, 2, 2)).setObjects(("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerPrimaryDnsIpAddress"), ("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", "trpzExtServerSecondaryDnsIpAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzExternalServerDnsServerGroup = trpzExternalServerDnsServerGroup.setStatus('current')
if mibBuilder.loadTexts: trpzExternalServerDnsServerGroup.setDescription('Group of objects implemented to provide DNS Server configuration info in releases 7.5 and greater.')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-EXTERNAL-SERVER-MIB", trpzExternalServerDataObjects=trpzExternalServerDataObjects, trpzExtServerPrimaryDnsIpAddress=trpzExtServerPrimaryDnsIpAddress, trpzExternalServerDnsServerGroup=trpzExternalServerDnsServerGroup, PYSNMP_MODULE_ID=trpzExternalServerMib, trpzExternalServerConfigGroup=trpzExternalServerConfigGroup, trpzExternalServerConformance=trpzExternalServerConformance, trpzExtServerSyslogPort=trpzExtServerSyslogPort, trpzExternalServerComplianceRev2=trpzExternalServerComplianceRev2, trpzExtServerSyslogIndex=trpzExtServerSyslogIndex, trpzExtServerSyslogEntry=trpzExtServerSyslogEntry, trpzExternalServerObjects=trpzExternalServerObjects, TrpzSyslogServerEnable=TrpzSyslogServerEnable, trpzExtServerSyslogAddress=trpzExtServerSyslogAddress, trpzExternalServerCompliances=trpzExternalServerCompliances, trpzExternalServerGroups=trpzExternalServerGroups, trpzExtServerSyslogEnable=trpzExtServerSyslogEnable, trpzExternalServerMib=trpzExternalServerMib, trpzExtServerSecondaryDnsIpAddress=trpzExtServerSecondaryDnsIpAddress, trpzExternalServerCompliance=trpzExternalServerCompliance, trpzExternalServerGlobalObjects=trpzExternalServerGlobalObjects, trpzExtServerSyslogTable=trpzExtServerSyslogTable)
