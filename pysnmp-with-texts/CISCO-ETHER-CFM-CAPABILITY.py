#
# PySNMP MIB module CISCO-ETHER-CFM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHER-CFM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, ModuleIdentity, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, TimeTicks, Gauge32, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "ModuleIdentity", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "TimeTicks", "Gauge32", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherCfmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 431))
ciscoEtherCfmMibCapability.setRevisions(('2005-02-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setLastUpdated('200502110000Z')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ethermibs@cisco.com')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setDescription('Agent capabilities for the CISCO-ETHER-CFM-MIB.')
ciscoEtherCfmMibCapabilityV122 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 431, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setProductRelease('Cisco IOS 12.2X (exact rev TBD)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapabilityV122.setDescription('CISCO-ETHER-CFM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ETHER-CFM-CAPABILITY", ciscoEtherCfmMibCapabilityV122=ciscoEtherCfmMibCapabilityV122, ciscoEtherCfmMibCapability=ciscoEtherCfmMibCapability, PYSNMP_MODULE_ID=ciscoEtherCfmMibCapability)
