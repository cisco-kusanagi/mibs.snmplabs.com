#
# PySNMP MIB module CISCO-ETHER-CFM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHER-CFM-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibIdentifier, iso, Counter64, Bits, ModuleIdentity, Integer32, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, IpAddress, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "Counter64", "Bits", "ModuleIdentity", "Integer32", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "IpAddress", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEtherCfmMibCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 431))
ciscoEtherCfmMibCapability.setRevisions(('2005-02-11 00:00',))
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setLastUpdated('200502110000Z')
if mibBuilder.loadTexts: ciscoEtherCfmMibCapability.setOrganization('Cisco Systems, Inc.')
ciscoEtherCfmMibCapabilityV122 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 431, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setProductRelease('Cisco IOS 12.2X (exact rev TBD)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherCfmMibCapabilityV122 = ciscoEtherCfmMibCapabilityV122.setStatus('current')
mibBuilder.exportSymbols("CISCO-ETHER-CFM-CAPABILITY", PYSNMP_MODULE_ID=ciscoEtherCfmMibCapability, ciscoEtherCfmMibCapabilityV122=ciscoEtherCfmMibCapabilityV122, ciscoEtherCfmMibCapability=ciscoEtherCfmMibCapability)
