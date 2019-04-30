#
# PySNMP MIB module CISCO-FTP-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FTP-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Gauge32, TimeTicks, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, Unsigned32, IpAddress, MibIdentifier, Integer32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "Integer32", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cftpclientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 483))
cftpclientCapability.setRevisions(('2006-01-02 00:00',))
if mibBuilder.loadTexts: cftpclientCapability.setLastUpdated('200601020000Z')
if mibBuilder.loadTexts: cftpclientCapability.setOrganization('Cisco Systems, Inc.')
cftpclientCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 483, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cftpclientCapabilityIOSXRV2R0CRS1 = cftpclientCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cftpclientCapabilityIOSXRV2R0CRS1 = cftpclientCapabilityIOSXRV2R0CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-FTP-CLIENT-CAPABILITY", cftpclientCapability=cftpclientCapability, PYSNMP_MODULE_ID=cftpclientCapability, cftpclientCapabilityIOSXRV2R0CRS1=cftpclientCapabilityIOSXRV2R0CRS1)
