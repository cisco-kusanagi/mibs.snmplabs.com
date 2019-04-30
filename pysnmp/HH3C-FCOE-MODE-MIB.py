#
# PySNMP MIB module HH3C-FCOE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FCOE-MODE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, ModuleIdentity, Counter64, iso, Integer32, IpAddress, Gauge32, ObjectIdentity, TimeTicks, Bits, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ModuleIdentity", "Counter64", "iso", "Integer32", "IpAddress", "Gauge32", "ObjectIdentity", "TimeTicks", "Bits", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cFcoeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 135))
hh3cFcoeMode.setRevisions(('2013-03-08 11:00',))
if mibBuilder.loadTexts: hh3cFcoeMode.setLastUpdated('201303081100Z')
if mibBuilder.loadTexts: hh3cFcoeMode.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cFcoeModeMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 135, 1))
hh3cFcoeModeCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFcoeModeCfgMode.setStatus('current')
hh3cFcoeModeCfgLastResult = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 135, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("noLicence", 2), ("needReset", 3), ("unknownFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFcoeModeCfgLastResult.setStatus('current')
mibBuilder.exportSymbols("HH3C-FCOE-MODE-MIB", hh3cFcoeModeMibObjects=hh3cFcoeModeMibObjects, PYSNMP_MODULE_ID=hh3cFcoeMode, hh3cFcoeModeCfgMode=hh3cFcoeModeCfgMode, hh3cFcoeModeCfgLastResult=hh3cFcoeModeCfgLastResult, hh3cFcoeMode=hh3cFcoeMode)
