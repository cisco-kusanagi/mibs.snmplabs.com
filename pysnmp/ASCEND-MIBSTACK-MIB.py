#
# PySNMP MIB module ASCEND-MIBSTACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSTACK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, ModuleIdentity, Counter64, Gauge32, iso, Bits, TimeTicks, Integer32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ModuleIdentity", "Counter64", "Gauge32", "iso", "Bits", "TimeTicks", "Integer32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibstackingProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 122))
mibstackingProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 122, 1), )
if mibBuilder.loadTexts: mibstackingProfileTable.setStatus('mandatory')
mibstackingProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1), ).setIndexNames((0, "ASCEND-MIBSTACK-MIB", "stackingProfile-Index-o"))
if mibBuilder.loadTexts: mibstackingProfileEntry.setStatus('mandatory')
stackingProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 1), Integer32()).setLabel("stackingProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: stackingProfile_Index_o.setStatus('mandatory')
stackingProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("stackingProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackingProfile_Enabled.setStatus('mandatory')
stackingProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 3), DisplayString()).setLabel("stackingProfile-Name").setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackingProfile_Name.setStatus('mandatory')
stackingProfile_UdpPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 4), Integer32()).setLabel("stackingProfile-UdpPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackingProfile_UdpPort.setStatus('mandatory')
stackingProfile_MulticastAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 5), IpAddress()).setLabel("stackingProfile-MulticastAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackingProfile_MulticastAddress.setStatus('mandatory')
stackingProfile_MulticastInterfaceIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 6), IpAddress()).setLabel("stackingProfile-MulticastInterfaceIpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackingProfile_MulticastInterfaceIpAddress.setStatus('mandatory')
stackingProfile_DataIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 7), IpAddress()).setLabel("stackingProfile-DataIpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackingProfile_DataIpAddress.setStatus('mandatory')
stackingProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 122, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("stackingProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackingProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSTACK-MIB", stackingProfile_Enabled=stackingProfile_Enabled, mibstackingProfileTable=mibstackingProfileTable, stackingProfile_MulticastInterfaceIpAddress=stackingProfile_MulticastInterfaceIpAddress, stackingProfile_Action_o=stackingProfile_Action_o, stackingProfile_UdpPort=stackingProfile_UdpPort, mibstackingProfileEntry=mibstackingProfileEntry, stackingProfile_DataIpAddress=stackingProfile_DataIpAddress, stackingProfile_Name=stackingProfile_Name, stackingProfile_Index_o=stackingProfile_Index_o, mibstackingProfile=mibstackingProfile, DisplayString=DisplayString, stackingProfile_MulticastAddress=stackingProfile_MulticastAddress)
