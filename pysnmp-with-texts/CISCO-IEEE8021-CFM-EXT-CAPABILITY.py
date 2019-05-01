#
# PySNMP MIB module CISCO-IEEE8021-CFM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IEEE8021-CFM-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:59:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Integer32, Counter64, TimeTicks, Unsigned32, IpAddress, NotificationType, Counter32, Gauge32, iso, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks", "Unsigned32", "IpAddress", "NotificationType", "Counter32", "Gauge32", "iso", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoIeee8021CfmExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 576))
ciscoIeee8021CfmExtCapability.setRevisions(('2008-12-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setLastUpdated('200812050000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setDescription('The capabilities description of CISCO-IEEE8021-CFM-EXT-MIB.')
ciscoIeee8021CfmExtCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 576, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setStatus('current')
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapCatOSV08R0702.setDescription('CISCO-IEEE8021-CFM-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-EXT-CAPABILITY", ciscoIeee8021CfmExtCapability=ciscoIeee8021CfmExtCapability, ciscoIeee8021CfmExtCapCatOSV08R0702=ciscoIeee8021CfmExtCapCatOSV08R0702, PYSNMP_MODULE_ID=ciscoIeee8021CfmExtCapability)
