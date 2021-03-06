#
# PySNMP MIB module DVB-MGSYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DVB-MGSYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:54:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Integer32, Counter64, Unsigned32, MibIdentifier, iso, enterprises, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Integer32", "Counter64", "Unsigned32", "MibIdentifier", "iso", "enterprises", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mgSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 2696, 3, 1))
if mibBuilder.loadTexts: mgSystem.setLastUpdated('200105181600Z')
if mibBuilder.loadTexts: mgSystem.setOrganization('DVB')
if mibBuilder.loadTexts: mgSystem.setContactInfo('DVB project European Broadcasting Union CH-1218 GRAND SACONNEX (Geneva) Switzerland Tel: +41 22 717 21 11 Fax: +41 22 717 24 81')
if mibBuilder.loadTexts: mgSystem.setDescription('DVB Measurement Group MIB to support TR 101 290. This mgSystem module contains general system information, similar to that provided by MIB-II.')
dvb = MibIdentifier((1, 3, 6, 1, 4, 1, 2696))
mg = MibIdentifier((1, 3, 6, 1, 4, 1, 2696, 3))
mgSysDescr = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgSysDescr.setStatus('current')
if mibBuilder.loadTexts: mgSysDescr.setDescription("A textual description of the entity. This value should include the full name and version identification of the system's hardware type, software operating-system, and networking software. It is mandatory that this only contain printable ASCII characters.")
mgSysObjectID = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgSysObjectID.setStatus('current')
if mibBuilder.loadTexts: mgSysObjectID.setDescription("The vendor's authoritative identification of the network management subsystem contained in the entity. This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining `what kind of box' is being managed. For example, if vendor `Flintstones, Inc.' was assigned the subtree 1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its `Fred Router'.")
mgSysUpTime = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgSysUpTime.setStatus('current')
if mibBuilder.loadTexts: mgSysUpTime.setDescription('The time (in hundredths of a second) since the network management portion of the system was last re-initialized.')
mgSysContact = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgSysContact.setStatus('current')
if mibBuilder.loadTexts: mgSysContact.setDescription('The textual identification of the contact person for this managed node, together with information on how to contact this person.')
mgSysName = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgSysName.setStatus('current')
if mibBuilder.loadTexts: mgSysName.setDescription("An administratively-assigned name for this managed node. By convention, this is the node's fully-qualified domain name.")
mgSysLocation = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgSysLocation.setStatus('current')
if mibBuilder.loadTexts: mgSysLocation.setDescription("The physical location of this node (e.g., `telephone closet, 3rd floor').")
mgSysServices = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgSysServices.setStatus('current')
if mibBuilder.loadTexts: mgSysServices.setDescription('A value which indicates the set of services that this entity primarily offers. The value is a sum. This sum initially takes the value zero, Then, for each layer, L, in the range 1 through 7, that this node performs transactions for, 2 raised to (L - 1) is added to the sum. For example, a node which performs primarily routing functions would have a value of 4 (2^(3-1)). In contrast, a node which is a host offering application services would have a value of 72 (2^(4-1) + 2^(7-1)). Note that in the context of the Internet suite of protocols, values should be calculated accordingly: layer functionality 1 physical (e.g., repeaters) 2 datalink/subnetwork (e.g., bridges) 3 internet (e.g., IP gateways) 4 end-to-end (e.g., IP hosts) 7 applications (e.g., mail relays) For systems including OSI protocols, layers 5 and 6 may also be counted.')
mgSysSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgSysSerialNumber.setStatus('current')
if mibBuilder.loadTexts: mgSysSerialNumber.setDescription('Manufacturer Serial Number')
mgSysVersion = MibScalar((1, 3, 6, 1, 4, 1, 2696, 3, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgSysVersion.setStatus('current')
if mibBuilder.loadTexts: mgSysVersion.setDescription('Manufacturer Version Number (hardware and software)')
mibBuilder.exportSymbols("DVB-MGSYSTEM-MIB", mgSysUpTime=mgSysUpTime, mg=mg, mgSysSerialNumber=mgSysSerialNumber, mgSysContact=mgSysContact, mgSysVersion=mgSysVersion, mgSysDescr=mgSysDescr, mgSysName=mgSysName, mgSysServices=mgSysServices, mgSysLocation=mgSysLocation, PYSNMP_MODULE_ID=mgSystem, dvb=dvb, mgSysObjectID=mgSysObjectID, mgSystem=mgSystem)
