#
# PySNMP MIB module NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, IpAddress, MibIdentifier, TimeTicks, Gauge32, Unsigned32, Bits, Counter64, ObjectIdentity, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "IpAddress", "MibIdentifier", "TimeTicks", "Gauge32", "Unsigned32", "Bits", "Counter64", "ObjectIdentity", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nnchassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2))
nnchassisMib.setRevisions(('1999-07-01 00:00',))
if mibBuilder.loadTexts: nnchassisMib.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: nnchassisMib.setOrganization('Nortel')
nnchassisType = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnchassisType.setStatus('current')
nnchassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnchassisSerialNumber.setStatus('current')
mibBuilder.exportSymbols("NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB", nnchassisType=nnchassisType, PYSNMP_MODULE_ID=nnchassisMib, nnchassisMib=nnchassisMib, nnchassisSerialNumber=nnchassisSerialNumber)
