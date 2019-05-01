#
# PySNMP MIB module CISCO-CONFIG-MAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONFIG-MAN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:53:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, Counter32, Gauge32, NotificationType, ModuleIdentity, Counter64, TimeTicks, Unsigned32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "Counter32", "Gauge32", "NotificationType", "ModuleIdentity", "Counter64", "TimeTicks", "Unsigned32", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cconfigManCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 469))
cconfigManCapability.setRevisions(('2005-12-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cconfigManCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cconfigManCapability.setLastUpdated('200512290000Z')
if mibBuilder.loadTexts: cconfigManCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cconfigManCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cconfigManCapability.setDescription('Agent capabilities for CISCO-CONFIG-MAN-MIB')
cconfigManCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 469, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cconfigManCapabilityIOSXRV2R0CRS1.setDescription('CISCO-CONFIG-MAN-MIB capabilities for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-CAPABILITY", cconfigManCapability=cconfigManCapability, cconfigManCapabilityIOSXRV2R0CRS1=cconfigManCapabilityIOSXRV2R0CRS1, PYSNMP_MODULE_ID=cconfigManCapability)
