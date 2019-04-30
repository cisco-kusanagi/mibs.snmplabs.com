#
# PySNMP MIB module HPN-ICF-OBJECT-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-OBJECT-INFO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Integer32, Unsigned32, NotificationType, Counter32, ObjectIdentity, Counter64, IpAddress, iso, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Integer32", "Unsigned32", "NotificationType", "Counter32", "ObjectIdentity", "Counter64", "IpAddress", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfObjectInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55))
hpnicfObjectInfo.setRevisions(('2004-12-27 00:00',))
if mibBuilder.loadTexts: hpnicfObjectInfo.setLastUpdated('200412270000Z')
if mibBuilder.loadTexts: hpnicfObjectInfo.setOrganization('')
hpnicfObjectInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1))
hpnicfObjectInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1), )
if mibBuilder.loadTexts: hpnicfObjectInfoTable.setStatus('current')
hpnicfObjectInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoOID"), (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoType"), (0, "HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTypeExtension"))
if mibBuilder.loadTexts: hpnicfObjectInfoEntry.setStatus('current')
hpnicfObjectInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: hpnicfObjectInfoOID.setStatus('current')
hpnicfObjectInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("reserved", 1), ("accessType", 2), ("dataType", 3), ("dataRange", 4), ("dataLength", 5))))
if mibBuilder.loadTexts: hpnicfObjectInfoType.setStatus('current')
hpnicfObjectInfoTypeExtension = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hpnicfObjectInfoTypeExtension.setStatus('current')
hpnicfObjectInfoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfObjectInfoValue.setStatus('current')
hpnicfObjectInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2))
hpnicfObjectInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1))
hpnicfObjectInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 1, 1)).setObjects(("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfObjectInfoMIBCompliance = hpnicfObjectInfoMIBCompliance.setStatus('current')
hpnicfObjectInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2))
hpnicfObjectInfoTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 55, 2, 2, 1)).setObjects(("HPN-ICF-OBJECT-INFO-MIB", "hpnicfObjectInfoValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpnicfObjectInfoTableGroup = hpnicfObjectInfoTableGroup.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-OBJECT-INFO-MIB", hpnicfObjectInfoMIBConformance=hpnicfObjectInfoMIBConformance, hpnicfObjectInfoMIBGroups=hpnicfObjectInfoMIBGroups, hpnicfObjectInfoMIBCompliance=hpnicfObjectInfoMIBCompliance, hpnicfObjectInfoEntry=hpnicfObjectInfoEntry, hpnicfObjectInfoType=hpnicfObjectInfoType, hpnicfObjectInfoTable=hpnicfObjectInfoTable, hpnicfObjectInfoMIBCompliances=hpnicfObjectInfoMIBCompliances, hpnicfObjectInformation=hpnicfObjectInformation, hpnicfObjectInfoOID=hpnicfObjectInfoOID, hpnicfObjectInfoValue=hpnicfObjectInfoValue, hpnicfObjectInfoTableGroup=hpnicfObjectInfoTableGroup, hpnicfObjectInfoTypeExtension=hpnicfObjectInfoTypeExtension, PYSNMP_MODULE_ID=hpnicfObjectInfo, hpnicfObjectInfo=hpnicfObjectInfo)
