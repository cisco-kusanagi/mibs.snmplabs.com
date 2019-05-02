#
# PySNMP MIB module CISCO-MOBILE-IP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MOBILE-IP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, Bits, TimeTicks, IpAddress, Gauge32, NotificationType, ObjectIdentity, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "ObjectIdentity", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMobileIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 449))
ciscoMobileIPCapability.setRevisions(('2005-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMobileIPCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMobileIPCapability.setLastUpdated('200509090000Z')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-mobileip@cisco.com')
if mibBuilder.loadTexts: ciscoMobileIPCapability.setDescription('Agent capabilities for CISCO-MOBILE-IP-MIB (MobileIP MIB).')
ciscoMobileIPCapabilityV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 449, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setProductRelease('Cisco IOS 12.4(3)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobileIPCapabilityV12R04 = ciscoMobileIPCapabilityV12R04.setStatus('current')
if mibBuilder.loadTexts: ciscoMobileIPCapabilityV12R04.setDescription('Cisco MobileIP mib capabilities')
mibBuilder.exportSymbols("CISCO-MOBILE-IP-CAPABILITY", ciscoMobileIPCapabilityV12R04=ciscoMobileIPCapabilityV12R04, ciscoMobileIPCapability=ciscoMobileIPCapability, PYSNMP_MODULE_ID=ciscoMobileIPCapability)
