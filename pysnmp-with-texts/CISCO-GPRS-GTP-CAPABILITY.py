#
# PySNMP MIB module CISCO-GPRS-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GPRS-GTP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, iso, Bits, NotificationType, MibIdentifier, ObjectIdentity, Counter64, Unsigned32, Integer32, Counter32, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "iso", "Bits", "NotificationType", "MibIdentifier", "ObjectIdentity", "Counter64", "Unsigned32", "Integer32", "Counter32", "Gauge32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cgprsGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 212))
cgprsGtpCapability.setRevisions(('2001-12-20 16:00', '2001-06-05 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cgprsGtpCapability.setRevisionsDescriptions(('Updated information for cgprsGtpDroppedPktsMonTime. ', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cgprsGtpCapability.setLastUpdated('200112201600Z')
if mibBuilder.loadTexts: cgprsGtpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cgprsGtpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-gprs@cisco.com')
if mibBuilder.loadTexts: cgprsGtpCapability.setDescription('Agent capabilities for CISCO-GPRS-GTP-MIB')
cgprsGtpCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setStatus('current')
if mibBuilder.loadTexts: cgprsGtpCapabilityV12R01.setDescription('Cisco GPRS GTP MIB capabilities.')
cgprsGtpCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setProductRelease('Cisco IOS 12.2(7)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setStatus('current')
if mibBuilder.loadTexts: cgprsGtpCapabilityV12R02.setDescription('Cisco GPRS GTP MIB capabilities.')
mibBuilder.exportSymbols("CISCO-GPRS-GTP-CAPABILITY", PYSNMP_MODULE_ID=cgprsGtpCapability, cgprsGtpCapabilityV12R01=cgprsGtpCapabilityV12R01, cgprsGtpCapabilityV12R02=cgprsGtpCapabilityV12R02, cgprsGtpCapability=cgprsGtpCapability)
