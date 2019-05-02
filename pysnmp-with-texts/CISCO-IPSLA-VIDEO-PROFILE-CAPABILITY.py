#
# PySNMP MIB module CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, NotificationType, Gauge32, MibIdentifier, TimeTicks, ModuleIdentity, Counter64, ObjectIdentity, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Counter64", "ObjectIdentity", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIpslaVideoProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 605))
ciscoIpslaVideoProfileCapability.setRevisions(('2011-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setLastUpdated('201106010000Z')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setDescription('Agent capabilities for CISCO-IPSLA-VIDEO-PROFILE-MIB')
ciscoIpslaVideoProfileCapabilityV152R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 605, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setStatus('current')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapabilityV152R02T.setDescription('Cisco IPSLA Video Profile MIB Capabilities in 15.2(2)T Release')
mibBuilder.exportSymbols("CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY", ciscoIpslaVideoProfileCapabilityV152R02T=ciscoIpslaVideoProfileCapabilityV152R02T, PYSNMP_MODULE_ID=ciscoIpslaVideoProfileCapability, ciscoIpslaVideoProfileCapability=ciscoIpslaVideoProfileCapability)
