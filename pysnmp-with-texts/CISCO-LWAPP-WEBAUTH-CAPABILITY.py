#
# PySNMP MIB module CISCO-LWAPP-WEBAUTH-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-WEBAUTH-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:06:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibIdentifier, Unsigned32, IpAddress, Counter64, ObjectIdentity, TimeTicks, NotificationType, Bits, Gauge32, Counter32, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "IpAddress", "Counter64", "ObjectIdentity", "TimeTicks", "NotificationType", "Bits", "Gauge32", "Counter32", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLwappWebauthCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 5555))
ciscoLwappWebauthCapability.setRevisions(('2010-07-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setLastUpdated('201007300000Z')
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappWebauthCapability.setDescription('Agent capabilities for CISCO-LWAPP-WEBAUTH-MIB.')
ciscoLwappWebAuthCapabilityCUWNSV7R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 5555, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWebAuthCapabilityCUWNSV7R0 = ciscoLwappWebAuthCapabilityCUWNSV7R0.setProductRelease('Cisco Unified Wireless Network Software\n                        Release 7.0 for Cisco WLAN Controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappWebAuthCapabilityCUWNSV7R0 = ciscoLwappWebAuthCapabilityCUWNSV7R0.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappWebAuthCapabilityCUWNSV7R0.setDescription('CiscoLwappWebAuthMIB capabilities')
mibBuilder.exportSymbols("CISCO-LWAPP-WEBAUTH-CAPABILITY", ciscoLwappWebauthCapability=ciscoLwappWebauthCapability, PYSNMP_MODULE_ID=ciscoLwappWebauthCapability, ciscoLwappWebAuthCapabilityCUWNSV7R0=ciscoLwappWebAuthCapabilityCUWNSV7R0)
