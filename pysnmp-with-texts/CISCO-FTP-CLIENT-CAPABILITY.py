#
# PySNMP MIB module CISCO-FTP-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FTP-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:58:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ModuleIdentity, Bits, NotificationType, iso, Unsigned32, IpAddress, MibIdentifier, Counter64, Gauge32, ObjectIdentity, Integer32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "NotificationType", "iso", "Unsigned32", "IpAddress", "MibIdentifier", "Counter64", "Gauge32", "ObjectIdentity", "Integer32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cftpclientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 483))
cftpclientCapability.setRevisions(('2006-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cftpclientCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: cftpclientCapability.setLastUpdated('200601020000Z')
if mibBuilder.loadTexts: cftpclientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cftpclientCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: cftpclientCapability.setDescription('The capabilities description of CISCO-FTP-CLIENT-MIB.')
cftpclientCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 483, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cftpclientCapabilityIOSXRV2R0CRS1 = cftpclientCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cftpclientCapabilityIOSXRV2R0CRS1 = cftpclientCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cftpclientCapabilityIOSXRV2R0CRS1.setDescription('CISCO-FTP-CLIENT-MIB capabilities for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-FTP-CLIENT-CAPABILITY", cftpclientCapability=cftpclientCapability, PYSNMP_MODULE_ID=cftpclientCapability, cftpclientCapabilityIOSXRV2R0CRS1=cftpclientCapabilityIOSXRV2R0CRS1)
