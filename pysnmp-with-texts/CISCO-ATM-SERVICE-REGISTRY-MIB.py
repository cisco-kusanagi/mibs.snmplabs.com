#
# PySNMP MIB module CISCO-ATM-SERVICE-REGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-SERVICE-REGISTRY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, ModuleIdentity, NotificationType, Counter64, Unsigned32, MibIdentifier, iso, TimeTicks, Gauge32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Counter64", "Unsigned32", "MibIdentifier", "iso", "TimeTicks", "Gauge32", "Counter32", "Bits")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoAtmServiceRegistryMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 50))
ciscoAtmServiceRegistryMIB.setRevisions(('1996-02-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setLastUpdated('9602210000Z')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAtmServiceRegistryMIB.setDescription("A MIB module to allow an NMS to monitor and configure the information which an ATM switch makes available via the ILMI's Service Registry Table.")
ciscoAtmServiceRegistryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 1))
class AtmAddr(TextualConvention, OctetString):
    description = 'The ATM address used by the network entity. The address types are: no address (0 octets), E.164 (8 octets), network prefix (13 octets), and NSAP (20 octets). Note: The E.164 address is encoded in BCD format.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
class InterfaceIndexOrZero(TextualConvention, Integer32):
    description = 'Either the value 0, or the ifIndex value of an ATM Interface.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

asrSrvcRegTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1), )
if mibBuilder.loadTexts: asrSrvcRegTable.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegTable.setDescription('The table implemented by an ATM switch to allow monitoring and control of the ATM addresses of registered services which it makes avaiable to ATM end-systems via the ILMI across its UNIs.')
asrSrvcRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1), ).setIndexNames((0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegPort"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegServiceID"), (0, "CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegAddressIndex"))
if mibBuilder.loadTexts: asrSrvcRegEntry.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegEntry.setDescription('Information about a single service provider that is to be made available to the user-side of one or more ATM UNIs. An entry, for which asrSrvcRegPort has a non-zero value, is a specific assignment to that UNI; an entry for which asrSrvcRegPort is zero applies to all UNIs for which this table contains no specific assignments.')
asrSrvcRegPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: asrSrvcRegPort.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegPort.setDescription('Either the value 0, or the ifIndex value of an the ATM Interface. A row for which this object has a non-zero value is a specific assignment to that UNI; a row for which this object is zero applies to all UNIs for which this table contains no specific assignments. Some switches may only support this object with the value of zero.')
asrSrvcRegServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: asrSrvcRegServiceID.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegServiceID.setDescription('The service identifier which uniquely identifies the type of service at the address given by the corresponding value of asrSrvcRegATMAddress. Specific values for this identifier are defined in the ILMI specification (e.g., asrSrvcRegLecs) or elsewhere.')
asrSrvcRegATMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 3), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegATMAddress.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegATMAddress.setDescription('An ATM address to which the ATM end-system on this UNI can attempt to establish a connection for the service.')
asrSrvcRegAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 4), Integer32())
if mibBuilder.loadTexts: asrSrvcRegAddressIndex.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegAddressIndex.setDescription('An arbitrary integer to differentiate multiple rows containing different ATM addresses for the same service on the same UNI.')
asrSrvcRegParm1 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegParm1.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegParm1.setDescription('An octet string used according to the value of asrSrvcRegServiceID.')
asrSrvcRegRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 50, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: asrSrvcRegRowStatus.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegRowStatus.setDescription("The status of this row. No object in the row can be modified while the value of this object is 'active'.")
asrSrvcRegMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3))
asrSrvcRegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1))
asrSrvcRegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2))
asrSrvcRegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 1, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBCompliance = asrSrvcRegMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegMIBCompliance.setDescription('The compliance statement for ATM switches which implement the Cisco Service Registry MIB')
asrSrvcRegMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 50, 3, 2, 1)).setObjects(("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegATMAddress"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegParm1"), ("CISCO-ATM-SERVICE-REGISTRY-MIB", "asrSrvcRegRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    asrSrvcRegMIBGroup = asrSrvcRegMIBGroup.setStatus('current')
if mibBuilder.loadTexts: asrSrvcRegMIBGroup.setDescription('A collection of objects providing monitoring and control of ATM addresses of services which an ATM switch is to make available via the ILMI.')
mibBuilder.exportSymbols("CISCO-ATM-SERVICE-REGISTRY-MIB", asrSrvcRegServiceID=asrSrvcRegServiceID, asrSrvcRegMIBConformance=asrSrvcRegMIBConformance, asrSrvcRegMIBGroup=asrSrvcRegMIBGroup, asrSrvcRegEntry=asrSrvcRegEntry, InterfaceIndexOrZero=InterfaceIndexOrZero, asrSrvcRegRowStatus=asrSrvcRegRowStatus, asrSrvcRegMIBCompliance=asrSrvcRegMIBCompliance, ciscoAtmServiceRegistryMIBObjects=ciscoAtmServiceRegistryMIBObjects, asrSrvcRegPort=asrSrvcRegPort, ciscoAtmServiceRegistryMIB=ciscoAtmServiceRegistryMIB, asrSrvcRegMIBGroups=asrSrvcRegMIBGroups, asrSrvcRegTable=asrSrvcRegTable, asrSrvcRegATMAddress=asrSrvcRegATMAddress, asrSrvcRegAddressIndex=asrSrvcRegAddressIndex, PYSNMP_MODULE_ID=ciscoAtmServiceRegistryMIB, asrSrvcRegParm1=asrSrvcRegParm1, asrSrvcRegMIBCompliances=asrSrvcRegMIBCompliances, AtmAddr=AtmAddr)
