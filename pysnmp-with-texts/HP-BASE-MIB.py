#
# PySNMP MIB module HP-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:33:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, Integer32, iso, Counter64, ObjectIdentity, MibIdentifier, IpAddress, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "Integer32", "iso", "Counter64", "ObjectIdentity", "MibIdentifier", "IpAddress", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpicfAccess = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 6))
hpicfAccess.setRevisions(('2005-01-31 13:55',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfAccess.setRevisionsDescriptions(('Modified to reflect new OID hierarchy for HP J8162A XL Access Controller Module.',))
if mibBuilder.loadTexts: hpicfAccess.setLastUpdated('200501311355Z')
if mibBuilder.loadTexts: hpicfAccess.setOrganization('Hewlett Packard Company, ProCurve Networking Business')
if mibBuilder.loadTexts: hpicfAccess.setContactInfo('Hewlett Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfAccess.setDescription('This MIB module describes devices in the HP Procurve 700 series product line.')
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
mibBuilder.exportSymbols("HP-BASE-MIB", hpicfAccess=hpicfAccess, hpEtherSwitch=hpEtherSwitch, icf=icf, hpSwitchJ4819A=hpSwitchJ4819A, nm=nm, hpProcurveCommon=hpProcurveCommon, netElement=netElement, hpicfObjects=hpicfObjects, hp=hp, hpSystem=hpSystem, hpSwitchModuleJ8162A=hpSwitchModuleJ8162A, PYSNMP_MODULE_ID=hpicfAccess)
