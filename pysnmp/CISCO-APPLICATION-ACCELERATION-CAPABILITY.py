#
# PySNMP MIB module CISCO-APPLICATION-ACCELERATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-APPLICATION-ACCELERATION-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Bits, Integer32, ModuleIdentity, Unsigned32, ObjectIdentity, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, iso, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Integer32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "iso", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAppAccCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 567))
ciscoAppAccCapability.setRevisions(('2008-07-29 00:00',))
if mibBuilder.loadTexts: ciscoAppAccCapability.setLastUpdated('200807290000Z')
if mibBuilder.loadTexts: ciscoAppAccCapability.setOrganization('Cisco Systems, Inc.')
ciscoAppAccCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 567, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7) for ACE \n                4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppAccCapc4710aceVA1R700 = ciscoAppAccCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPLICATION-ACCELERATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoAppAccCapability, ciscoAppAccCapc4710aceVA1R700=ciscoAppAccCapc4710aceVA1R700, ciscoAppAccCapability=ciscoAppAccCapability)
