#
# PySNMP MIB module CISCO-CONFIG-MAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONFIG-MAN-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, Bits, Gauge32, Unsigned32, iso, ModuleIdentity, TimeTicks, MibIdentifier, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cconfigManCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 469))
cconfigManCapability.setRevisions(('2005-12-29 00:00',))
if mibBuilder.loadTexts: cconfigManCapability.setLastUpdated('200512290000Z')
if mibBuilder.loadTexts: cconfigManCapability.setOrganization('Cisco Systems, Inc.')
cconfigManCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 469, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cconfigManCapabilityIOSXRV2R0CRS1 = cconfigManCapabilityIOSXRV2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONFIG-MAN-CAPABILITY", PYSNMP_MODULE_ID=cconfigManCapability, cconfigManCapabilityIOSXRV2R0CRS1=cconfigManCapabilityIOSXRV2R0CRS1, cconfigManCapability=cconfigManCapability)
