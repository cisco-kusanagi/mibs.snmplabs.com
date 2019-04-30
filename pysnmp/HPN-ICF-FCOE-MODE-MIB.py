#
# PySNMP MIB module HPN-ICF-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FCOE-MODE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, IpAddress, Bits, ModuleIdentity, Counter32, Unsigned32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "IpAddress", "Bits", "ModuleIdentity", "Counter32", "Unsigned32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135))
hpnicfFcoeMode.setRevisions(('2013-03-08 11:00',))
if mibBuilder.loadTexts: hpnicfFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: hpnicfFcoeMode.setOrganization('')
hpnicfFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1))
hpnicfFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgMode.setStatus('current')
hpnicfFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFcoeModeCfgLastResult.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FCOE-MODE-MIB", PYSNMP_MODULE_ID=hpnicfFcoeMode, hpnicfFcoeModeCfgLastResult=hpnicfFcoeModeCfgLastResult, hpnicfFcoeModeMibObjects=hpnicfFcoeModeMibObjects, hpnicfFcoeMode=hpnicfFcoeMode, hpnicfFcoeModeCfgMode=hpnicfFcoeModeCfgMode)
