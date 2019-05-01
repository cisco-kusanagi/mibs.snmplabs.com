#
# PySNMP MIB module NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ntEnterpriseDataTasmanMgmt, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Gauge32, Unsigned32, Integer32, IpAddress, MibIdentifier, iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "Unsigned32", "Integer32", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nnchassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2))
nnchassisMib.setRevisions(('1999-07-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nnchassisMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: nnchassisMib.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: nnchassisMib.setOrganization('Nortel')
if mibBuilder.loadTexts: nnchassisMib.setContactInfo(' ')
if mibBuilder.loadTexts: nnchassisMib.setDescription('Listing and brief description of product model numbers.')
nnchassisType = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnchassisType.setStatus('current')
if mibBuilder.loadTexts: nnchassisType.setDescription('The chassis type.')
nnchassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnchassisSerialNumber.setStatus('current')
if mibBuilder.loadTexts: nnchassisSerialNumber.setDescription('The serial number of the chassis.')
mibBuilder.exportSymbols("NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB", nnchassisType=nnchassisType, nnchassisSerialNumber=nnchassisSerialNumber, PYSNMP_MODULE_ID=nnchassisMib, nnchassisMib=nnchassisMib)
