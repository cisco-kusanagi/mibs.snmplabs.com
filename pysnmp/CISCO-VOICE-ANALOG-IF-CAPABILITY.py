#
# PySNMP MIB module CISCO-VOICE-ANALOG-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-ANALOG-IF-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, TimeTicks, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Counter32, Counter64, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "TimeTicks", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Counter32", "Counter64", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceAnalogIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 82))
ciscoVoiceAnalogIfCapability.setRevisions(('2003-04-28 00:00', '1997-06-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setLastUpdated('200304280000Z')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setOrganization('Cisco Systems, Inc.')
ciscoVoiceAnalogIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 82, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-ANALOG-IF-CAPABILITY", ciscoVoiceAnalogIfCapability=ciscoVoiceAnalogIfCapability, PYSNMP_MODULE_ID=ciscoVoiceAnalogIfCapability, ciscoVoiceAnalogIfCapabilityV11R03=ciscoVoiceAnalogIfCapabilityV11R03)
