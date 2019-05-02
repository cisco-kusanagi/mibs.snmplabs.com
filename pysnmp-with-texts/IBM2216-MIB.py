#
# PySNMP MIB module IBM2216-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM2216-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:51:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, TimeTicks, Counter64, Unsigned32, IpAddress, Integer32, Counter32, NotificationType, enterprises, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "TimeTicks", "Counter64", "Unsigned32", "IpAddress", "Integer32", "Counter32", "NotificationType", "enterprises", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm2216 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131))
ibm2216admin = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1))
ibm2216system = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 2))
ibm2216hardware = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 3))
ibm2216routing = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 4))
ibm2216switching = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 5))
ibm2216adminproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 1))
ibm2216mod400 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 1, 1))
ibm2216adminOID = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2))
ibm2216adminDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 3))
ibm2216systemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 2, 1))
ibm2216cfgInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 2, 2))
ibm2216hardwareGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1))
ibm2216hardware400Specific = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 2))
ibm2216EnetChipSet = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2, 1))
enetChipSetToshiba = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2, 1, 1))
enetChipSetAMD = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 131, 1, 2, 1, 2))
ibm2216PCIAdapTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1), )
if mibBuilder.loadTexts: ibm2216PCIAdapTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216PCIAdapTable.setDescription('A table of information about PCI adapters in this box.')
ibm2216PCIAdapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1), ).setIndexNames((0, "IBM2216-MIB", "ibm2216PCIAdapSlotNum"))
if mibBuilder.loadTexts: ibm2216PCIAdapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216PCIAdapEntry.setDescription('An entry containing objects to describe the adapter in a given slot.')
ibm2216PCIAdapSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibm2216PCIAdapSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216PCIAdapSlotNum.setDescription('The number identifying a slot location where an adapter can be inserted.')
ibm2216PCIAdapType = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("unknown", 1), ("not-present", 2), ("atm-mmf-lic294", 3), ("atm-mmf-lic284", 4), ("atm-smf-lic295", 5), ("atm-smf-lic293", 6), ("token-ring-lic280", 7), ("escon-lic287", 8), ("isdn-t1j1-lic283", 9), ("isdn-e1-lic292", 10), ("serial-rs232-lic282", 11), ("serial-v35-lic290", 12), ("serial-x21-lic291", 13), ("ethernet-lic281", 14), ("ethernet-fast-lic288", 15), ("serial-hssi-lic289", 16), ("fddi-lic286", 17), ("isdn-t1j1-lic297", 18), ("isdn-e1-lic298", 19), ("parallel-channel-lic299", 20)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibm2216PCIAdapType.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216PCIAdapType.setDescription('The type of adapter that is inserted into this slot. If no adapter is present, the variable will take the value not-present(2).')
ibm2216PCIAdapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("unknown", 1), ("not-configured", 2), ("not-present", 3), ("does-not-apply", 4), ("enable-pending", 5), ("enabled", 6), ("disable-pending", 7), ("disabled", 8), ("not-initialized", 9), ("unknown-device", 10), ("hardware-error", 11), ("not-powered", 12), ("diagnostics", 13), ("wrs-available", 14), ("mis-configured", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibm2216PCIAdapOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216PCIAdapOperStatus.setDescription('The operational status of this PCI adapter. unknown (1) : If there was problem determining the operational status of the adapter. not-configured (2) : If the adapter inserted in the slot is recognized but no router configuration exists. not-present (3) : If no adapter is currently inserted. does-not-apply (4) : If this adapter does not contain an operational state. enable-pending (5) : If commands have been issued to enable the adapter but have not been completed. enabled (6) : If commands have been successfully issued to enable the adapter. disable-pending (7) : If commands have been issued to disable the adapter but have not been completed. disabled (8) : If commands have been successfully issued to disable the adapter. not-initialized (9) : If the adapter has not completed its initialization. unknown-device (10) : If the adapter inserted in the slot can not be recognized. hardware-error (11) : If the adapter can not be used nor made ready to be used. not-powered (12) : If the adapter has had a problem obtaining power from its slot. diagnostics (13) : If the adapter is currently undergoing diagnostics. wrs-available (14) : If the adapter is currently configured and available for WAN restoral. mis-configured (15) : If the adapter is inserted in the slot but the router configuration is of a different type.')
ibm2216GraphicTable = MibTable((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2), )
if mibBuilder.loadTexts: ibm2216GraphicTable.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216GraphicTable.setDescription('A table of information mapping a slot and port to an interface table ifIndex. An entry exists in this table only if the ifConnectorPresent object is true')
ibm2216GraphicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1), ).setIndexNames((0, "IBM2216-MIB", "ibm2216GraphicSlotNum"), (0, "IBM2216-MIB", "ibm2216GraphicPortNum"))
if mibBuilder.loadTexts: ibm2216GraphicEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216GraphicEntry.setDescription('An entry mapping slot and port to an interface table ifIndex.')
ibm2216GraphicSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibm2216GraphicSlotNum.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216GraphicSlotNum.setDescription('The number identifying a slot location where an adapter can be inserted.')
ibm2216GraphicPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibm2216GraphicPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216GraphicPortNum.setDescription('The number identifying a port on a given adapter. A port implies a physical connector is associated with it.')
ibm2216GraphicifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2, 6, 131, 3, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibm2216GraphicifIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ibm2216GraphicifIndex.setDescription('The ifIndex of the interface table entry associated with this port on an adapter. By definition, the ifEntry has ifConnectorPresent = true.')
mibBuilder.exportSymbols("IBM2216-MIB", ibmProd=ibmProd, enetChipSetAMD=enetChipSetAMD, ibm2216routing=ibm2216routing, ibm2216GraphicSlotNum=ibm2216GraphicSlotNum, ibm2216admin=ibm2216admin, ibm2216PCIAdapTable=ibm2216PCIAdapTable, ibm2216switching=ibm2216switching, ibm=ibm, ibm2216adminOID=ibm2216adminOID, ibm2216GraphicEntry=ibm2216GraphicEntry, ibm2216cfgInfo=ibm2216cfgInfo, ibm2216PCIAdapEntry=ibm2216PCIAdapEntry, ibm2216adminproducts=ibm2216adminproducts, ibm2216hardware=ibm2216hardware, ibm2216hardware400Specific=ibm2216hardware400Specific, ibm2216PCIAdapType=ibm2216PCIAdapType, ibm2216GraphicTable=ibm2216GraphicTable, ibm2216=ibm2216, ibm2216mod400=ibm2216mod400, ibm2216GraphicifIndex=ibm2216GraphicifIndex, ibm2216EnetChipSet=ibm2216EnetChipSet, ibm2216system=ibm2216system, ibm2216adminDebug=ibm2216adminDebug, ibm2216systemInfo=ibm2216systemInfo, enetChipSetToshiba=enetChipSetToshiba, ibm2216GraphicPortNum=ibm2216GraphicPortNum, ibm2216hardwareGeneral=ibm2216hardwareGeneral, ibm2216PCIAdapSlotNum=ibm2216PCIAdapSlotNum, ibm2216PCIAdapOperStatus=ibm2216PCIAdapOperStatus)
