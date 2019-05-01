#
# PySNMP MIB module HPN-ICF-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FCOE-MODE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, iso, Integer32, ObjectIdentity, Unsigned32, Counter64, NotificationType, Counter32, Bits, IpAddress, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "iso", "Integer32", "ObjectIdentity", "Unsigned32", "Counter64", "NotificationType", "Counter32", "Bits", "IpAddress", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135))
hpnicfFcoeMode.setRevisions(('2013-03-08 11:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfFcoeMode.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: hpnicfFcoeMode.setOrganization('')
if mibBuilder.loadTexts: hpnicfFcoeMode.setContactInfo('')
if mibBuilder.loadTexts: hpnicfFcoeMode.setDescription('This MIB module is for configuring and monitoring the working mode of FCoE (Fibre Channel over Ethernet) features.')
hpnicfFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1))
hpnicfFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfFcoeModeCfgMode.setDescription('This object specifies the FCoE modes the switch supports. The object has four available values: 1: non-FCoE mode. 2: FCF mode. 3: NPV mode. 4: Transit mode. The switch mode can only be converted from non-FCoE mode to one of FCoE modes, or vice versa, but cannot be converted directly among the other three FCoE modes. To convert among the other three FCoE modes, the switch should first be converted to non-FCoE mode. After converting the switch to non-FCoE mode, FCoE-related configurations in the original FCoE mode will be cleared.')
hpnicfFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgLastResult.setStatus('current')
if mibBuilder.loadTexts: hpnicfFcoeModeCfgLastResult.setDescription('This object specifies the result of the latest FCoE mode configuration. The object has four values: success - Configured successfully. noLicence - Configured unsuccessfully for lack of licence. needReset - Configured unsuccessfully, because the desired mode is not non-FCoE mode, and the mode should be first set to non-FCoE mode. unknownFault - Configured unsuccessfully for unknown fault.')
mibBuilder.exportSymbols("HPN-ICF-FCOE-MODE-MIB", hpnicfFcoeMode=hpnicfFcoeMode, PYSNMP_MODULE_ID=hpnicfFcoeMode, hpnicfFcoeModeMibObjects=hpnicfFcoeModeMibObjects, hpnicfFcoeModeCfgMode=hpnicfFcoeModeCfgMode, hpnicfFcoeModeCfgLastResult=hpnicfFcoeModeCfgLastResult)
