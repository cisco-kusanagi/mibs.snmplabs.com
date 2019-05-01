#
# PySNMP MIB module HH3C-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FCOE-MODE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, Bits, ModuleIdentity, Gauge32, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, TimeTicks, Counter32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Bits", "ModuleIdentity", "Gauge32", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "TimeTicks", "Counter32", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 135))
hh3cFcoeMode.setRevisions(('2013-03-08 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cFcoeMode.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hh3cFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: hh3cFcoeMode.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cFcoeMode.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cFcoeMode.setDescription('This MIB module is for configuring and monitoring the working mode of FCoE (Fibre Channel over Ethernet) features.')
hh3cFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 135, 1))
hh3cFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcoeModeCfgMode.setStatus('current')
if mibBuilder.loadTexts: hh3cFcoeModeCfgMode.setDescription('This object specifies the FCoE modes the switch supports. The object has four available values: 1: non-FCoE mode. 2: FCF mode. 3: NPV mode. 4: Transit mode. The switch mode can only be converted from non-FCoE mode to one of FCoE modes, or vice versa, but cannot be converted directly among the other three FCoE modes. To convert among the other three FCoE modes, the switch should first be converted to non-FCoE mode. After converting the switch to non-FCoE mode, FCoE-related configurations in the original FCoE mode will be cleared.')
hh3cFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcoeModeCfgLastResult.setStatus('current')
if mibBuilder.loadTexts: hh3cFcoeModeCfgLastResult.setDescription('This object specifies the result of the latest FCoE mode configuration. The object has four values: success - Configured successfully. noLicence - Configured unsuccessfully for lack of licence. needReset - Configured unsuccessfully, because the desired mode is not non-FCoE mode, and the mode should be first set to non-FCoE mode. unknownFault - Configured unsuccessfully for unknown fault.')
mibBuilder.exportSymbols("HH3C-FCOE-MODE-MIB", hh3cFcoeModeCfgMode=hh3cFcoeModeCfgMode, hh3cFcoeMode=hh3cFcoeMode, hh3cFcoeModeCfgLastResult=hh3cFcoeModeCfgLastResult, PYSNMP_MODULE_ID=hh3cFcoeMode, hh3cFcoeModeMibObjects=hh3cFcoeModeMibObjects)
