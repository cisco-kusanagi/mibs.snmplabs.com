#
# PySNMP MIB module PDN-MPD-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPD-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
pdnMpdExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnMpdExt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, Unsigned32, Gauge32, IpAddress, iso, ModuleIdentity, Counter64, NotificationType, ObjectIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Unsigned32", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnMpdExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1))
if mibBuilder.loadTexts: pdnMpdExtMIB.setLastUpdated('200304081900Z')
if mibBuilder.loadTexts: pdnMpdExtMIB.setOrganization('Paradyne Corporation MIB Working Group')
if mibBuilder.loadTexts: pdnMpdExtMIB.setContactInfo(' Paradyne Networks Inc. Postal: 8545, 126th Ave. N. Largo, FL 33779 US Editor: Jesus Pinto Email: mibwg_team@eng.paradyne.com')
if mibBuilder.loadTexts: pdnMpdExtMIB.setDescription('This management information module supports the objects that extend the Message Processing Dispatcher mib as described in rfc3412_std62_a.mib.')
pdnMpdExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1))
pdnMpdExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2))
class PdnMpdExtSecurityMode(TextualConvention, Bits):
    description = 'A set of combinations of Model and SecurityLevel that can be supported by an agent. An agent can support more than a single combination at once. Bit 0 : None. - SNMP access is not allowed. Bit 1 : SNMPv1, noAuthNoPriv. - SNMPv1 access is allowed with - no auth and no privacy. - Only Security checking based on community names is performed. Bit 2 : SNMPv2c, no AuthNoPriv. - SNMPv2c access is allowed with - no auth and no privacy. - Only Security checking based on community names is performed. Bit 3 : SNMPv3, noAuthNoPriv. - SNMPv3 access is allowed with - no auth and no privacy. Bit 4 : SNMPv3, AuthNoPriv. - SNMPv3 access is allowed with - authentication and no privacy. Bit 5 : SNMPv3, AuthPriv. - SNMPv3 access is allowed with - authentication and privacy. '
    status = 'current'
    namedValues = NamedValues(("none", 0), ("snmpv1NoAuthNoPriv", 1), ("snmpv2cNoAuthNoPriv", 2), ("snmpv3NoAuthNoPriv", 3), ("snmpv3AuthNoPriv", 4), ("snmpv3AuthPriv", 5))

pdnMpdExtSecurityModeConfig = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1, 1), PdnMpdExtSecurityMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMpdExtSecurityModeConfig.setStatus('current')
if mibBuilder.loadTexts: pdnMpdExtSecurityModeConfig.setDescription('This object is used to configure the level of SNMP access that the agent supports. That is, which combinations of Model Processing can be dispatched and what security levels are supported for those models. An agent can choose to support more than a single combination of modes, (e.g., SNMPv1 and SNMPv2 with noAuthNoPriv) or choose to support a single option (e.g., a very secured agent with only SNMPv3 with authentication and privacy enabled.). Even some of these combinations may not be supported at all. Setting this object to a valid value will cause the entries associated with those Models and SecurityLevels being changed to become active/inactive in tables processed by the SNMPv3 Framework. ')
pdnMpdExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1))
pdnMpdExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2))
pdnMpdExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1, 1)).setObjects(("PDN-MPD-EXT-MIB", "pdnMpdExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMpdExtCompliance = pdnMpdExtCompliance.setStatus('current')
if mibBuilder.loadTexts: pdnMpdExtCompliance.setDescription('The compliance statement for MPD extension mib.')
pdnMpdExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2, 1)).setObjects(("PDN-MPD-EXT-MIB", "pdnMpdExtSecurityModeConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMpdExtGroup = pdnMpdExtGroup.setStatus('current')
if mibBuilder.loadTexts: pdnMpdExtGroup.setDescription('A collection of configuration objects applicable to MPD extention.')
mibBuilder.exportSymbols("PDN-MPD-EXT-MIB", pdnMpdExtCompliances=pdnMpdExtCompliances, pdnMpdExtSecurityModeConfig=pdnMpdExtSecurityModeConfig, pdnMpdExtMIB=pdnMpdExtMIB, PYSNMP_MODULE_ID=pdnMpdExtMIB, pdnMpdExtMIBObjects=pdnMpdExtMIBObjects, pdnMpdExtGroup=pdnMpdExtGroup, pdnMpdExtGroups=pdnMpdExtGroups, pdnMpdExtMIBConformance=pdnMpdExtMIBConformance, pdnMpdExtCompliance=pdnMpdExtCompliance, PdnMpdExtSecurityMode=PdnMpdExtSecurityMode)
