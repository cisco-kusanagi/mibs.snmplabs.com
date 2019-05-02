#
# PySNMP MIB module CISCO-IETF-NAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-NAT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Counter64, Integer32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Bits, Counter32, Unsigned32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Counter64", "Integer32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Bits", "Counter32", "Unsigned32", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIetfNatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoIetfNatCapability.setRevisions(('2001-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfNatCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfNatCapability.setLastUpdated('200109100000Z')
if mibBuilder.loadTexts: ciscoIetfNatCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfNatCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-nat@cisco.com')
if mibBuilder.loadTexts: ciscoIetfNatCapability.setDescription('Agent capabilities for NAT-MIB')
ciscoIetfNatCapabilityV12R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfNatCapabilityV12R02T = ciscoIetfNatCapabilityV12R02T.setProductRelease('Cisco IOS 12.2T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfNatCapabilityV12R02T = ciscoIetfNatCapabilityV12R02T.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfNatCapabilityV12R02T.setDescription('NAT MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-NAT-CAPABILITY", ciscoIetfNatCapabilityV12R02T=ciscoIetfNatCapabilityV12R02T, ciscoIetfNatCapability=ciscoIetfNatCapability, PYSNMP_MODULE_ID=ciscoIetfNatCapability)
