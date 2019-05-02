#
# PySNMP MIB module CISCO-ITP-SCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-SCCP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
IpAddress, Counter32, Integer32, Counter64, NotificationType, iso, TimeTicks, ModuleIdentity, Gauge32, MibIdentifier, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Integer32", "Counter64", "NotificationType", "iso", "TimeTicks", "ModuleIdentity", "Gauge32", "MibIdentifier", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoItpSccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 221))
ciscoItpSccpCapability.setRevisions(('2002-03-04 00:00', '2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpSccpCapability.setRevisionsDescriptions(('Changes required for the following modifications to the CISCO-ITP-SCCP-MIB. Added the following objects: CItpSccpGttPrefName cItpSccpPrefConfigLastChanged cItpSccpGttPrePrefConv cItpSccpGttPostPrefConv cItpSccpGttGtaAddrDispZB cItpSccpGttGtaAddrLenZB cItpSccpGttGtaAsName Added the following Tables: cItpSccpGttAppGrTable cItpSccpGttPrefTable Updated the following Textual Conventions: CItpSccpGttAppType CItpSccpGttGtaResType Deprecated the following objects: CItpSccpGttGtaAddrLen cItpSccpGttGtaAddrDisp cItpSccpGttGtaAddrLen Deprecated the following Tables: cItpSccpGttAppTable', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpSccpCapability.setLastUpdated('200203040000Z')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpSccpCapability.setDescription('Agent capabilities for the CISCO-ITP-SCCP-MIB.')
ciscoItpSccpCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R024MB1 = ciscoItpSccpCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSccpCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-SCCP-MIB.my User Agent MIB capabilities.')
ciscoItpSccpCapabilityV12R0204MB4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 221, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setProductRelease('Cisco IOS 12.2(4)MB4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpSccpCapabilityV12R0204MB4 = ciscoItpSccpCapabilityV12R0204MB4.setStatus('current')
if mibBuilder.loadTexts: ciscoItpSccpCapabilityV12R0204MB4.setDescription('IOS 12.2(4)MB4 Cisco CISCO-ITP-SCCP-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-SCCP-CAPABILITY", ciscoItpSccpCapabilityV12R024MB1=ciscoItpSccpCapabilityV12R024MB1, ciscoItpSccpCapability=ciscoItpSccpCapability, ciscoItpSccpCapabilityV12R0204MB4=ciscoItpSccpCapabilityV12R0204MB4, PYSNMP_MODULE_ID=ciscoItpSccpCapability)
