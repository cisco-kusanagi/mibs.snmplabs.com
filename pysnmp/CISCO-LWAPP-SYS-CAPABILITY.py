#
# PySNMP MIB module CISCO-LWAPP-SYS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-SYS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Bits, Counter64, MibIdentifier, Gauge32, IpAddress, ObjectIdentity, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "Gauge32", "IpAddress", "ObjectIdentity", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLwappSysCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 3333))
ciscoLwappSysCapability.setRevisions(('2010-08-17 00:00',))
if mibBuilder.loadTexts: ciscoLwappSysCapability.setLastUpdated('201008170000Z')
if mibBuilder.loadTexts: ciscoLwappSysCapability.setOrganization('Cisco Systems, Inc.')
ciscoLwappSysCapabilityCUWNSR7V0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.0 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V0 = ciscoLwappSysCapabilityCUWNSR7V0.setStatus('current')
ciscoLwappSysCapabilityCUWNSR7V2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 3333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setProductRelease('Cisco Unified Wireless Network Software\n                     Release 7.2 for Cisco WLAN controllers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappSysCapabilityCUWNSR7V2 = ciscoLwappSysCapabilityCUWNSR7V2.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-SYS-CAPABILITY", ciscoLwappSysCapabilityCUWNSR7V2=ciscoLwappSysCapabilityCUWNSR7V2, PYSNMP_MODULE_ID=ciscoLwappSysCapability, ciscoLwappSysCapabilityCUWNSR7V0=ciscoLwappSysCapabilityCUWNSR7V0, ciscoLwappSysCapability=ciscoLwappSysCapability)
