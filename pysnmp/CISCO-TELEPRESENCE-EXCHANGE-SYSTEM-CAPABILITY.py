#
# PySNMP MIB module CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, Bits, Counter32, Unsigned32, IpAddress, Gauge32, ModuleIdentity, MibIdentifier, ObjectIdentity, Integer32, TimeTicks, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Counter32", "Unsigned32", "IpAddress", "Gauge32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceExchangeSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 615))
ciscoTelepresenceExchangeSystemCapability.setRevisions(('2013-04-11 00:00', '2012-08-17 00:00',))
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setLastUpdated('201304150000Z')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setOrganization('Cisco Systems, Inc.')
ciscoTelepresenceCapabilityCTXV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.2.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setStatus('current')
ciscoTelepresenceCapabilityCTXV130 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.3.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setStatus('current')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY", ciscoTelepresenceExchangeSystemCapability=ciscoTelepresenceExchangeSystemCapability, ciscoTelepresenceCapabilityCTXV120=ciscoTelepresenceCapabilityCTXV120, ciscoTelepresenceCapabilityCTXV130=ciscoTelepresenceCapabilityCTXV130, PYSNMP_MODULE_ID=ciscoTelepresenceExchangeSystemCapability)
