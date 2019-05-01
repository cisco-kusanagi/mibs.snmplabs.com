#
# PySNMP MIB module CISCO-DIST-DIRECTOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIST-DIRECTOR-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Bits, IpAddress, Unsigned32, ModuleIdentity, ObjectIdentity, TimeTicks, iso, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "iso", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDistDirCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 267))
ciscoDistDirCapability.setRevisions(('2002-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDistDirCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDistDirCapability.setLastUpdated('200204230000Z')
if mibBuilder.loadTexts: ciscoDistDirCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDistDirCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dd@cisco.com')
if mibBuilder.loadTexts: ciscoDistDirCapability.setDescription('Agent capabilities for CISCO-DIST-DIRECTOR-MIB')
ciscoDistDirCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 267, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setProductRelease('Cisco IOS 12.2(8)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDistDirCapabilityV12R02 = ciscoDistDirCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: ciscoDistDirCapabilityV12R02.setDescription('Cisco Distributed Director MIB capabilities')
mibBuilder.exportSymbols("CISCO-DIST-DIRECTOR-CAPABILITY", ciscoDistDirCapability=ciscoDistDirCapability, ciscoDistDirCapabilityV12R02=ciscoDistDirCapabilityV12R02, PYSNMP_MODULE_ID=ciscoDistDirCapability)
