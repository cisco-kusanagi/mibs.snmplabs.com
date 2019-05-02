#
# PySNMP MIB module CISCO-IETF-ISIS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-ISIS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, NotificationType, IpAddress, Unsigned32, Counter32, Counter64, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "NotificationType", "IpAddress", "Unsigned32", "Counter32", "Counter64", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIetfIsisCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 446))
ciscoIetfIsisCapability.setRevisions(('2005-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfIsisCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setLastUpdated('200508180000Z')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-clns@cisco.com')
if mibBuilder.loadTexts: ciscoIetfIsisCapability.setDescription('Agent capabilities for CISCO-IETF-ISIS-MIB')
ciscoIetfIsisCapV12R0225SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 446, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setProductRelease('Cisco IOS 12.2(25)SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfIsisCapV12R0225SG = ciscoIetfIsisCapV12R0225SG.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfIsisCapV12R0225SG.setDescription('Cisco IS-IS MIB Agent Capabilities for IOS 12.2S')
mibBuilder.exportSymbols("CISCO-IETF-ISIS-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfIsisCapability, ciscoIetfIsisCapability=ciscoIetfIsisCapability, ciscoIetfIsisCapV12R0225SG=ciscoIetfIsisCapV12R0225SG)
