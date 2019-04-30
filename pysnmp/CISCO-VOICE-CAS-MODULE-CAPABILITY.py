#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-CAS-MODULE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ObjectIdentity, Bits, Counter32, IpAddress, Integer32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Gauge32, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Counter32", "IpAddress", "Integer32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Gauge32", "TimeTicks", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceCasModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 401))
ciscoVoiceCasModuleCapability.setRevisions(('2004-03-29 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setLastUpdated('200403290000Z')
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setOrganization('Cisco Systems, Inc.')
cvcmCapabilityV321 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 401, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setProductRelease('Cisco VISM Release 3.2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceCasModuleCapability, ciscoVoiceCasModuleCapability=ciscoVoiceCasModuleCapability, cvcmCapabilityV321=cvcmCapabilityV321)
