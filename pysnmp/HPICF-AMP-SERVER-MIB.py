#
# PySNMP MIB module HPICF-AMP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPICF-AMP-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:24:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, NotificationType, TimeTicks, Bits, Gauge32, ObjectIdentity, IpAddress, Counter64, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "NotificationType", "TimeTicks", "Bits", "Gauge32", "ObjectIdentity", "IpAddress", "Counter64", "MibIdentifier", "Counter32")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
hpicfAMPServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125))
hpicfAMPServerMIB.setRevisions(('2017-03-07 00:00', '2017-01-04 00:00', '2016-12-16 00:00', '2016-09-15 00:00', '2016-04-19 00:00', '2016-03-03 00:00', '2015-12-14 00:00',))
if mibBuilder.loadTexts: hpicfAMPServerMIB.setLastUpdated('201703070000Z')
if mibBuilder.loadTexts: hpicfAMPServerMIB.setOrganization('HP Networking')
hpicfAMPServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1))
hpicfAMPServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2))
hpicfArubaVPNObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3))
hpicfArubaVPNDefaultGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 4))
class HpicfArubaVPNType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("amp", 2), ("any", 3))

hpicfArubaVPNTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1), )
if mibBuilder.loadTexts: hpicfArubaVPNTable.setStatus('current')
hpicfArubaVPNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1), ).setIndexNames((0, "HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIndex"))
if mibBuilder.loadTexts: hpicfArubaVPNEntry.setStatus('current')
hpicfArubaVPNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 1), HpicfArubaVPNType())
if mibBuilder.loadTexts: hpicfArubaVPNIndex.setStatus('current')
hpicfArubaVPNRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfArubaVPNRowStatus.setStatus('current')
hpicfArubaVPNIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 3), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNIPType.setStatus('current')
hpicfArubaVPNIP = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 4), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNIP.setStatus('current')
hpicfArubaVPNTos = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNTos.setStatus('current')
hpicfArubaVPNTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNTtl.setStatus('current')
hpicfArubaVPNBkpIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 7), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNBkpIPType.setStatus('current')
hpicfArubaVPNBkpIP = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 3, 1, 1, 8), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNBkpIP.setStatus('current')
hpicfArubaVPNGateway = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfArubaVPNGateway.setStatus('current')
hpicfAMPServerIPType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerIPType.setStatus('current')
hpicfAMPServerIP = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerIP.setStatus('current')
hpicfAMPServerGroup = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerGroup.setStatus('current')
hpicfAMPServerFolder = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerFolder.setStatus('current')
hpicfAMPServerSecret = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerSecret.setStatus('current')
hpicfAMPServerConfigStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configured", 1), ("notConfigured", 2))).clone('notConfigured')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfAMPServerConfigStatus.setStatus('current')
hpicfAMPServerMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1))
hpicfAMPServerMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2))
hpicfAMPServerMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 1)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerMIBCompliance = hpicfAMPServerMIBCompliance.setStatus('deprecated')
hpicfAMPServerMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 2)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfDefaultGatewayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerMIBCompliance1 = hpicfAMPServerMIBCompliance1.setStatus('deprecated')
hpicfAMPServerMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 1, 3)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNConfigGroup1"), ("HPICF-AMP-SERVER-MIB", "hpicfDefaultGatewayGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerMIBCompliance2 = hpicfAMPServerMIBCompliance2.setStatus('current')
hpicfAMPServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 1)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfAMPServerIP"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerGroup"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerFolder"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerSecret"), ("HPICF-AMP-SERVER-MIB", "hpicfAMPServerConfigStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfAMPServerConfigGroup = hpicfAMPServerConfigGroup.setStatus('current')
hpicfArubaVPNConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 2)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNRowStatus"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIP"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTos"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTtl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfArubaVPNConfigGroup = hpicfArubaVPNConfigGroup.setStatus('deprecated')
hpicfDefaultGatewayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 3)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNGateway"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDefaultGatewayGroup = hpicfDefaultGatewayGroup.setStatus('current')
hpicfArubaVPNConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125, 2, 2, 4)).setObjects(("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNRowStatus"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNIP"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTos"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNTtl"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNBkpIPType"), ("HPICF-AMP-SERVER-MIB", "hpicfArubaVPNBkpIP"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfArubaVPNConfigGroup1 = hpicfArubaVPNConfigGroup1.setStatus('current')
mibBuilder.exportSymbols("HPICF-AMP-SERVER-MIB", hpicfArubaVPNObjects=hpicfArubaVPNObjects, hpicfArubaVPNRowStatus=hpicfArubaVPNRowStatus, hpicfAMPServerConfigGroup=hpicfAMPServerConfigGroup, hpicfAMPServerIP=hpicfAMPServerIP, hpicfArubaVPNEntry=hpicfArubaVPNEntry, hpicfArubaVPNDefaultGateway=hpicfArubaVPNDefaultGateway, hpicfAMPServerMIBCompliance1=hpicfAMPServerMIBCompliance1, hpicfAMPServerObjects=hpicfAMPServerObjects, hpicfArubaVPNConfigGroup=hpicfArubaVPNConfigGroup, hpicfAMPServerMIBCompliance=hpicfAMPServerMIBCompliance, hpicfArubaVPNIP=hpicfArubaVPNIP, HpicfArubaVPNType=HpicfArubaVPNType, hpicfArubaVPNIndex=hpicfArubaVPNIndex, hpicfAMPServerConfigStatus=hpicfAMPServerConfigStatus, hpicfAMPServerSecret=hpicfAMPServerSecret, hpicfArubaVPNConfigGroup1=hpicfArubaVPNConfigGroup1, hpicfArubaVPNTtl=hpicfArubaVPNTtl, hpicfArubaVPNTable=hpicfArubaVPNTable, hpicfDefaultGatewayGroup=hpicfDefaultGatewayGroup, hpicfAMPServerGroup=hpicfAMPServerGroup, hpicfAMPServerMIBCompliance2=hpicfAMPServerMIBCompliance2, hpicfAMPServerMIBCompliances=hpicfAMPServerMIBCompliances, hpicfArubaVPNBkpIPType=hpicfArubaVPNBkpIPType, hpicfAMPServerIPType=hpicfAMPServerIPType, hpicfArubaVPNTos=hpicfArubaVPNTos, PYSNMP_MODULE_ID=hpicfAMPServerMIB, hpicfAMPServerMIBGroups=hpicfAMPServerMIBGroups, hpicfAMPServerConformance=hpicfAMPServerConformance, hpicfArubaVPNBkpIP=hpicfArubaVPNBkpIP, hpicfAMPServerMIB=hpicfAMPServerMIB, hpicfArubaVPNGateway=hpicfArubaVPNGateway, hpicfAMPServerFolder=hpicfAMPServerFolder, hpicfArubaVPNIPType=hpicfArubaVPNIPType)
