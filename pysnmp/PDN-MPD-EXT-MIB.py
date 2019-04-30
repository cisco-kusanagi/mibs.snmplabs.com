#
# PySNMP MIB module PDN-MPD-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPD-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
pdnMpdExt, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnMpdExt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, Gauge32, Integer32, iso, Counter32, ModuleIdentity, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Gauge32", "Integer32", "iso", "Counter32", "ModuleIdentity", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnMpdExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1))
if mibBuilder.loadTexts: pdnMpdExtMIB.setLastUpdated('200304081900Z')
if mibBuilder.loadTexts: pdnMpdExtMIB.setOrganization('Paradyne Corporation MIB Working Group')
pdnMpdExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1))
pdnMpdExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2))
class PdnMpdExtSecurityMode(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("none", 0), ("snmpv1NoAuthNoPriv", 1), ("snmpv2cNoAuthNoPriv", 2), ("snmpv3NoAuthNoPriv", 3), ("snmpv3AuthNoPriv", 4), ("snmpv3AuthPriv", 5))

pdnMpdExtSecurityModeConfig = MibScalar((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 1, 1), PdnMpdExtSecurityMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnMpdExtSecurityModeConfig.setStatus('current')
pdnMpdExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1))
pdnMpdExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2))
pdnMpdExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 1, 1)).setObjects(("PDN-MPD-EXT-MIB", "pdnMpdExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMpdExtCompliance = pdnMpdExtCompliance.setStatus('current')
pdnMpdExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 44, 1, 2, 2, 1)).setObjects(("PDN-MPD-EXT-MIB", "pdnMpdExtSecurityModeConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnMpdExtGroup = pdnMpdExtGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-MPD-EXT-MIB", pdnMpdExtGroup=pdnMpdExtGroup, pdnMpdExtMIBConformance=pdnMpdExtMIBConformance, pdnMpdExtSecurityModeConfig=pdnMpdExtSecurityModeConfig, pdnMpdExtCompliance=pdnMpdExtCompliance, pdnMpdExtCompliances=pdnMpdExtCompliances, pdnMpdExtGroups=pdnMpdExtGroups, PYSNMP_MODULE_ID=pdnMpdExtMIB, PdnMpdExtSecurityMode=PdnMpdExtSecurityMode, pdnMpdExtMIB=pdnMpdExtMIB, pdnMpdExtMIBObjects=pdnMpdExtMIBObjects)
