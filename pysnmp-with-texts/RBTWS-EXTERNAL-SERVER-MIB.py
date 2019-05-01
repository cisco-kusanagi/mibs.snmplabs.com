#
# PySNMP MIB module RBTWS-EXTERNAL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-EXTERNAL-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:53:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Unsigned32, ModuleIdentity, TimeTicks, Counter64, ObjectIdentity, NotificationType, Integer32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter64", "ObjectIdentity", "NotificationType", "Integer32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsExternalServerMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7))
rbtwsExternalServerMib.setRevisions(('2006-07-31 00:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsExternalServerMib.setRevisionsDescriptions(('v1.0.4: Initial version, for 6.0 release',))
if mibBuilder.loadTexts: rbtwsExternalServerMib.setLastUpdated('200609271237Z')
if mibBuilder.loadTexts: rbtwsExternalServerMib.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsExternalServerMib.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsExternalServerMib.setDescription("External Server configuration MIB. Copyright 2006 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class RbtwsIpPort(TextualConvention, Unsigned32):
    description = 'An UDP or TCP port number.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class RbtwsSyslogServerEnable(TextualConvention, Integer32):
    description = 'Syslog Server mode (administratively enabled or disabled).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

rbtwsExternalServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1))
rbtwsExternalServerDataObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1))
rbtwsExtServerSyslogTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1), )
if mibBuilder.loadTexts: rbtwsExtServerSyslogTable.setStatus('current')
if mibBuilder.loadTexts: rbtwsExtServerSyslogTable.setDescription('Configured Syslog server table.')
rbtwsExtServerSyslogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1), ).setIndexNames((0, "RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogIndex"))
if mibBuilder.loadTexts: rbtwsExtServerSyslogEntry.setStatus('current')
if mibBuilder.loadTexts: rbtwsExtServerSyslogEntry.setDescription('Entry for Syslog server table.')
rbtwsExtServerSyslogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: rbtwsExtServerSyslogIndex.setStatus('current')
if mibBuilder.loadTexts: rbtwsExtServerSyslogIndex.setDescription('Index of the Syslog sever')
rbtwsExtServerSyslogAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogAddress.setStatus('current')
if mibBuilder.loadTexts: rbtwsExtServerSyslogAddress.setDescription('IP Address of the Syslog server.')
rbtwsExtServerSyslogPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 3), RbtwsIpPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogPort.setStatus('current')
if mibBuilder.loadTexts: rbtwsExtServerSyslogPort.setDescription('The Syslog server Port number.')
rbtwsExtServerSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 1, 1, 1, 4), RbtwsSyslogServerEnable()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbtwsExtServerSyslogEnable.setStatus('current')
if mibBuilder.loadTexts: rbtwsExtServerSyslogEnable.setDescription('The administrative status of the Syslog server (enabled/disabled)')
rbtwsExternalServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2))
rbtwsExternalServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1))
rbtwsExternalServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2))
rbtwsExternalServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 1, 1)).setObjects(("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExternalServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsExternalServerCompliance = rbtwsExternalServerCompliance.setStatus('current')
if mibBuilder.loadTexts: rbtwsExternalServerCompliance.setDescription('The compliance statement for devices that implement the External Server MIB.')
rbtwsExternalServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 7, 1, 2, 2, 1)).setObjects(("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogAddress"), ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogPort"), ("RBTWS-EXTERNAL-SERVER-MIB", "rbtwsExtServerSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbtwsExternalServerConfigGroup = rbtwsExternalServerConfigGroup.setStatus('current')
if mibBuilder.loadTexts: rbtwsExternalServerConfigGroup.setDescription('Mandatory group of objects implemented to provide External Server configuration info.')
mibBuilder.exportSymbols("RBTWS-EXTERNAL-SERVER-MIB", RbtwsIpPort=RbtwsIpPort, rbtwsExternalServerGroups=rbtwsExternalServerGroups, rbtwsExternalServerDataObjects=rbtwsExternalServerDataObjects, rbtwsExternalServerMib=rbtwsExternalServerMib, rbtwsExternalServerCompliances=rbtwsExternalServerCompliances, rbtwsExternalServerObjects=rbtwsExternalServerObjects, RbtwsSyslogServerEnable=RbtwsSyslogServerEnable, rbtwsExtServerSyslogPort=rbtwsExtServerSyslogPort, rbtwsExtServerSyslogEnable=rbtwsExtServerSyslogEnable, rbtwsExternalServerConformance=rbtwsExternalServerConformance, rbtwsExtServerSyslogTable=rbtwsExtServerSyslogTable, rbtwsExternalServerCompliance=rbtwsExternalServerCompliance, PYSNMP_MODULE_ID=rbtwsExternalServerMib, rbtwsExtServerSyslogIndex=rbtwsExtServerSyslogIndex, rbtwsExtServerSyslogAddress=rbtwsExtServerSyslogAddress, rbtwsExternalServerConfigGroup=rbtwsExternalServerConfigGroup, rbtwsExtServerSyslogEntry=rbtwsExtServerSyslogEntry)
