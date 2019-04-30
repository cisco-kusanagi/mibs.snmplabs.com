#
# PySNMP MIB module CISCO-BGP-POLICY-ACCOUNTING-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-BGP-POLICY-ACCOUNTING-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:33:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, ModuleIdentity, Unsigned32, Bits, iso, Gauge32, Counter64, MibIdentifier, IpAddress, NotificationType, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "ModuleIdentity", "Unsigned32", "Bits", "iso", "Gauge32", "Counter64", "MibIdentifier", "IpAddress", "NotificationType", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cbpAcctCapabilitity = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 468))
cbpAcctCapabilitity.setRevisions(('2005-12-30 00:00',))
if mibBuilder.loadTexts: cbpAcctCapabilitity.setLastUpdated('200512300000Z')
if mibBuilder.loadTexts: cbpAcctCapabilitity.setOrganization('Cisco Systems, Inc.')
cbgppaCapabilityIOSXRV3R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 468, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbgppaCapabilityIOSXRV3R0CRS1 = cbgppaCapabilityIOSXRV3R0CRS1.setProductRelease('Cisco IOS XR 3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbgppaCapabilityIOSXRV3R0CRS1 = cbgppaCapabilityIOSXRV3R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-BGP-POLICY-ACCOUNTING-MIB-CAPABILITY", PYSNMP_MODULE_ID=cbpAcctCapabilitity, cbpAcctCapabilitity=cbpAcctCapabilitity, cbgppaCapabilityIOSXRV3R0CRS1=cbgppaCapabilityIOSXRV3R0CRS1)
