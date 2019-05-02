#
# PySNMP MIB module CISCO-ITP-ACL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ITP-ACL-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:03:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, MibIdentifier, NotificationType, Integer32, IpAddress, iso, TimeTicks, Gauge32, ObjectIdentity, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "NotificationType", "Integer32", "IpAddress", "iso", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoItpAclCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 214))
ciscoItpAclCapability.setRevisions(('2001-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoItpAclCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoItpAclCapability.setLastUpdated('200110240000Z')
if mibBuilder.loadTexts: ciscoItpAclCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoItpAclCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoItpAclCapability.setDescription('Agent capabilities for the CISCO-ITP-ACL-MIB.')
ciscoItpAclCapabilityV12R024MB1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 214, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpAclCapabilityV12R024MB1 = ciscoItpAclCapabilityV12R024MB1.setProductRelease('Cisco IOS 12.2(4)MB1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoItpAclCapabilityV12R024MB1 = ciscoItpAclCapabilityV12R024MB1.setStatus('current')
if mibBuilder.loadTexts: ciscoItpAclCapabilityV12R024MB1.setDescription('IOS 12.2(4)MB1 Cisco CISCO-ITP-ACL-MIB.my User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ITP-ACL-CAPABILITY", ciscoItpAclCapability=ciscoItpAclCapability, PYSNMP_MODULE_ID=ciscoItpAclCapability, ciscoItpAclCapabilityV12R024MB1=ciscoItpAclCapabilityV12R024MB1)
