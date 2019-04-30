#
# PySNMP MIB module CISCO-VOIP-TAP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOIP-TAP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, MibIdentifier, Counter32, Bits, NotificationType, TimeTicks, Integer32, Counter64, Unsigned32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "Bits", "NotificationType", "TimeTicks", "Integer32", "Counter64", "Unsigned32", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoipTapCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 593))
ciscoVoipTapCapability.setRevisions(('2010-08-24 00:00',))
if mibBuilder.loadTexts: ciscoVoipTapCapability.setLastUpdated('201008240000Z')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setOrganization('Cisco Systems, Inc.')
ciscoVoipTapCapV15R01SXE31ASR1K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 593, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setProductRelease('Cisco IOS XE 15.0(01)SXE31 on ASR 1000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-CAPABILITY", ciscoVoipTapCapability=ciscoVoipTapCapability, PYSNMP_MODULE_ID=ciscoVoipTapCapability, ciscoVoipTapCapV15R01SXE31ASR1K=ciscoVoipTapCapV15R01SXE31ASR1K)
