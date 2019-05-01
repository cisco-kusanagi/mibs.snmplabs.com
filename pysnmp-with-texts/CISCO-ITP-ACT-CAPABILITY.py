#
# PySNMP MIB module CISCO-ITP-ACT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-ACT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, Bits, ModuleIdentity, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, NotificationType, iso, Counter32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "ModuleIdentity", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "NotificationType", "iso", "Counter32", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpActCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 219))
ciscoItpActCapability.setRevisions(('2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpActCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpActCapability.setLastUpdated('200110240000Z')
if mibBuilder.loadTexts: ciscoItpActCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpActCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpActCapability.setDescription('Agent capabilities for the CISCO-ITP-ACT-MIB.')
ciscoItpActCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 219, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpActCapabilityV12R024MB1 = ciscoItpActCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpActCapabilityV12R024MB1 = ciscoItpActCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpActCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-ACT-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-ACT-CAPABILITY", PYSNMP_MODULE_ID=ciscoItpActCapability, ciscoItpActCapabilityV12R024MB1=ciscoItpActCapabilityV12R024MB1, ciscoItpActCapability=ciscoItpActCapability)
