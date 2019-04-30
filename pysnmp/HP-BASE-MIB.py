#
# PySNMP MIB module HP-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Bits, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Counter64, NotificationType, TimeTicks, Gauge32, Integer32, ObjectIdentity, MibIdentifier, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "Integer32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfAccess = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 6))
hpicfAccess.setRevisions(('2005-01-31 13:55',))
if mibBuilder.loadTexts: hpicfAccess.setLastUpdated('200501311355Z')
if mibBuilder.loadTexts: hpicfAccess.setOrganization('Hewlett Packard Company, ProCurve Networking Business')
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
icf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14))
hpicfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11))
hpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3))
netElement = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7))
hpEtherSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11))
hpSwitchJ4819A = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17))
hpSwitchModuleJ8162A = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7))
hpProcurveCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7, 1))
mibBuilder.exportSymbols("HP-BASE-MIB", hpicfAccess=hpicfAccess, hpSystem=hpSystem, icf=icf, hp=hp, hpicfObjects=hpicfObjects, hpSwitchModuleJ8162A=hpSwitchModuleJ8162A, hpEtherSwitch=hpEtherSwitch, PYSNMP_MODULE_ID=hpicfAccess, hpSwitchJ4819A=hpSwitchJ4819A, hpProcurveCommon=hpProcurveCommon, nm=nm, netElement=netElement)
